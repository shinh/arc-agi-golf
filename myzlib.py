"""A tiny (and slow) DEFLATE encoder.

This module implements just enough of the DEFLATE format to create
zlib-compatible compressed streams.  It is intentionally written for
clarity rather than performance and supports only a single block using
*dynamically generated* Huffman code tables as described in RFC 1951.

The :func:`compress` function accepts ``bytes`` or ``str`` and returns a
``bytes`` object which can be fed to :func:`zlib.decompress`.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
import heapq
import builtins
import keyword
import random
import string
import warnings
from collections import Counter, namedtuple
from typing import Dict, Iterable, List, Tuple, Union

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _adler32(data: bytes) -> int:
    """Compute the Adler‑32 checksum of *data*.

    The algorithm maintains two sums ``a`` and ``b`` modulo 65521 and
    combines them into a single 32‑bit integer ``(b << 16) | a``.
    """

    MOD = 65521
    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD
        b = (b + a) % MOD
    return (b << 16) | a


def _reverse_bits(value: int, width: int) -> int:
    """Return ``value`` with ``width`` bits reversed (LSB <-> MSB)."""

    result = 0
    for _ in range(width):
        result = (result << 1) | (value & 1)
        value >>= 1
    return result


def _build_codes(lengths: List[int]) -> List[Tuple[int, int]]:
    """Build canonical Huffman codes from a list of bit ``lengths``.

    The return value is a list where ``codes[symbol]`` gives a pair
    ``(code, bit_length)`` for that symbol.  Code bits are already
    reversed so that they can be written to the bit stream LSB first.
    """

    max_bits = max(lengths)
    bl_count = [0] * (max_bits + 1)
    for l in lengths:
        if l:
            bl_count[l] += 1

    next_code = [0] * (max_bits + 1)
    code = 0
    for bits in range(1, max_bits + 1):
        code = (code + bl_count[bits - 1]) << 1
        next_code[bits] = code

    codes: List[Tuple[int, int]] = [(0, 0)] * len(lengths)
    for symbol, length in enumerate(lengths):
        if length:
            code = next_code[length]
            next_code[length] += 1
            codes[symbol] = (_reverse_bits(code, length), length)
    return codes


def _huffman_lengths(freqs: List[int], max_bits: int = 15) -> List[int]:
    """Compute Huffman code lengths from symbol ``freqs``.

    A minimal Huffman tree is built using a priority queue.  For the
    purposes of this educational implementation no explicit limit on the
    maximum bit length is enforced; the caller is expected to provide
    inputs that yield trees of depth ``<= max_bits``.
    """

    heap: List[Tuple[int, int, object]] = []
    for sym, freq in enumerate(freqs):
        if freq > 0:
            heap.append((freq, len(heap), sym))
    if not heap:
        return [0] * len(freqs)
    if len(heap) == 1:
        lengths = [0] * len(freqs)
        lengths[heap[0][2]] = 1
        return lengths
    heapq.heapify(heap)

    counter = len(heap)
    while len(heap) > 1:
        f1, _, n1 = heapq.heappop(heap)
        f2, _, n2 = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, counter, (n1, n2)))
        counter += 1

    lengths = [0] * len(freqs)

    def walk(node: object, depth: int) -> None:
        if isinstance(node, int):
            lengths[node] = depth
        else:
            left, right = node
            walk(left, depth + 1)
            walk(right, depth + 1)

    walk(heap[0][2], 0)
    return lengths


# Order in which code length code lengths are written in the stream
CODE_LENGTH_ORDER = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]


def _rle_code_lengths(
    lengths: List[int],
) -> Tuple[List[Union[int, Tuple[int, int]]], List[int]]:
    """Run‑length encode ``lengths`` and return (sequence, freq_table)."""

    rle: List[Union[int, Tuple[int, int]]] = []
    freq = [0] * 19
    i = 0
    n = len(lengths)
    while i < n:
        cur = lengths[i]
        run = 1
        while i + run < n and lengths[i + run] == cur:
            run += 1
        total = run
        if cur == 0:
            while run >= 11:
                cnt = min(run, 138)
                rle.append((18, cnt - 11))
                freq[18] += 1
                run -= cnt
            if run >= 3:
                rle.append((17, run - 3))
                freq[17] += 1
                run = 0
            while run > 0:
                rle.append(0)
                freq[0] += 1
                run -= 1
        else:
            rle.append(cur)
            freq[cur] += 1
            run -= 1
            while run >= 3:
                cnt = min(run, 6)
                rle.append((16, cnt - 3))
                freq[16] += 1
                run -= cnt
            while run > 0:
                rle.append(cur)
                freq[cur] += 1
                run -= 1
        i += total
    return rle, freq


def _write_dynamic_header(
    lit_lengths: List[int], dist_lengths: List[int], writer: _BitWriter
) -> None:
    """Write the dynamic Huffman header for the given code lengths."""

    # Determine how many codes we actually need to transmit.  Trailing
    # zero-length codes can be omitted.
    hlit = max(257, max(i for i, l in enumerate(lit_lengths) if l > 0) + 1)
    hdist = max(1, max(i for i, l in enumerate(dist_lengths) if l > 0) + 1)

    writer.write(hlit - 257, 5)
    writer.write(hdist - 1, 5)

    # Concatenate lengths and encode them using the code-length alphabet.
    combined = lit_lengths[:hlit] + dist_lengths[:hdist]
    rle, cl_freq = _rle_code_lengths(combined)

    cl_lengths = _huffman_lengths(cl_freq, 7)
    cl_codes = _build_codes(cl_lengths)

    # Determine how many code length codes to transmit.
    hclen = max(
        4, max(i for i, sym in enumerate(CODE_LENGTH_ORDER) if cl_lengths[sym] > 0) + 1
    )
    writer.write(hclen - 4, 4)
    for sym in CODE_LENGTH_ORDER[:hclen]:
        writer.write(cl_lengths[sym], 3)

    for item in rle:
        if isinstance(item, tuple):
            sym, extra = item
            code, length = cl_codes[sym]
            writer.write(code, length)
            if sym == 16:
                writer.write(extra, 2)
            elif sym == 17:
                writer.write(extra, 3)
            else:
                writer.write(extra, 7)
        else:
            code, length = cl_codes[item]
            writer.write(code, length)


# Tables describing length and distance code ranges.  Each entry contains
# (base value, number of extra bits).
LENGTH_BASE = [
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    13,
    15,
    17,
    19,
    23,
    27,
    31,
    35,
    43,
    51,
    59,
    67,
    83,
    99,
    115,
    131,
    163,
    195,
    227,
    258,
]
LENGTH_EXTRA = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    3,
    3,
    3,
    3,
    4,
    4,
    4,
    4,
    5,
    5,
    5,
    5,
    0,
]

DIST_BASE = [
    1,
    2,
    3,
    4,
    5,
    7,
    9,
    13,
    17,
    25,
    33,
    49,
    65,
    97,
    129,
    193,
    257,
    385,
    513,
    769,
    1025,
    1537,
    2049,
    3073,
    4097,
    6145,
    8193,
    12289,
    16385,
    24577,
]
DIST_EXTRA = [
    0,
    0,
    0,
    0,
    1,
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    5,
    5,
    6,
    6,
    7,
    7,
    8,
    8,
    9,
    9,
    10,
    10,
    11,
    11,
    12,
    12,
    13,
    13,
]


def _length_code(length: int) -> Tuple[int, int, int]:
    """Return the (code, extra_bits, extra_value) for a match ``length``."""

    for idx, base in enumerate(LENGTH_BASE):
        extra = LENGTH_EXTRA[idx]
        max_len = base + (1 << extra) - 1
        if length <= max_len:
            return 257 + idx, extra, length - base
    raise ValueError("invalid match length")


def _distance_code(dist: int) -> Tuple[int, int, int]:
    """Return the (code, extra_bits, extra_value) for a match distance."""

    for idx, base in enumerate(DIST_BASE):
        extra = DIST_EXTRA[idx]
        max_dist = base + (1 << extra) - 1
        if dist <= max_dist:
            return idx, extra, dist - base
    raise ValueError("invalid distance")


@dataclass
class Match:
    length: int
    distance: int


def _find_match(data: bytes, pos: int) -> Match:
    """Find the longest backward match for ``data[pos:]``.

    The search is extremely naive: it scans the previous 32 KiB of data
    for the longest match.  This is perfectly adequate for small inputs
    but exponentially slow for large ones.
    """

    end = len(data)
    best_len = 0
    best_dist = 0
    window_start = max(0, pos - 32768)

    for j in range(window_start, pos):
        length = 0
        while (
            length < 258
            and pos + length < end
            and data[j + length] == data[pos + length]
        ):
            length += 1
        if length > best_len and length >= 3:
            best_len = length
            best_dist = pos - j
            if length == 258:
                break
    return Match(best_len, best_dist)


class _BitWriter:
    """Helper for writing bits LSB-first to a bytearray."""

    def __init__(self, out: bytearray) -> None:
        self.out = out
        self.buf = 0
        self.nbits = 0

    def write(self, value: int, count: int) -> None:
        while count:
            self.buf |= (value & 1) << self.nbits
            value >>= 1
            self.nbits += 1
            if self.nbits == 8:
                self.out.append(self.buf)
                self.buf = 0
                self.nbits = 0
            count -= 1

    def flush(self) -> None:
        if self.nbits:
            self.out.append(self.buf)
            self.buf = 0
            self.nbits = 0


Position = namedtuple("Position", ["name", "lineno", "col_offset", "end_lineno", "end_col_offset", "kind"])


def get_identifier_positions(source_code: str) -> List[Position]:
    """Return positions of all identifiers found in *source_code*.

    Each element of the returned list is a tuple
    ``(name, lineno, col_offset, end_lineno, end_col_offset, kind)`` where
    ``kind`` describes the AST context (``"name"``, ``"attr"``, ``"func"``
    etc.).  Having the kind available later allows the caller to avoid
    touching attribute names which could otherwise change semantics.
    """

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=SyntaxWarning)
        tree = ast.parse(source_code)
    positions = []
    lines = source_code.splitlines()

    class IdentifierVisitor(ast.NodeVisitor):
        """Collect identifier occurrences with their location and kind."""

        def record(self, node, name, kind, lineno=None, col_offset=None):
            """Record *name* occurring at the given position and *kind*.

            ``lineno`` and ``col_offset`` default to the values from ``node``.
            They can be provided explicitly for cases where the AST node's
            position does not directly point at the identifier (e.g. function
            and class definitions where ``node.col_offset`` references the
            ``def``/``class`` keyword).  Identifier names never span multiple
            lines, so ``end_lineno`` is identical to ``lineno`` and ``end``
            positions are computed from ``col_offset`` and ``len(name)``.
            """

            if hasattr(node, "lineno") and hasattr(node, "col_offset"):
                lineno = lineno if lineno is not None else node.lineno
                col_offset = col_offset if col_offset is not None else node.col_offset
                end_lineno = lineno
                end_col_offset = col_offset + len(name)
                positions.append(Position(name, lineno, col_offset, end_lineno, end_col_offset, kind))

        def visit_Name(self, node):
            self.record(node, node.id, "name")
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            line = lines[node.lineno - 1]
            # ``node.col_offset`` points to the ``def`` keyword.  Search for the
            # actual function name after this keyword to avoid capturing the
            # "d" from ``def`` when the function name itself is also ``d``.
            start = node.col_offset + 4  # len("def ")
            col = line.find(node.name, start)
            self.record(node, node.name, "func", lineno=node.lineno, col_offset=col)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):
            line = lines[node.lineno - 1]
            # ``async def`` spans two keywords.  Skip both to locate the function
            # name correctly and avoid renaming parts of the keywords.
            start = node.col_offset + 10  # len("async def ")
            col = line.find(node.name, start)
            self.record(node, node.name, "func", lineno=node.lineno, col_offset=col)
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            line = lines[node.lineno - 1]
            # ``class`` is followed by a space before the class name.  Start the
            # search after that to ensure the name's position is correct.
            start = node.col_offset + 6  # len("class ")
            col = line.find(node.name, start)
            self.record(node, node.name, "class", lineno=node.lineno, col_offset=col)
            self.generic_visit(node)

        def visit_Attribute(self, node):
            self.record(node, node.attr, "attr")
            self.generic_visit(node)

        def visit_arg(self, node):
            self.record(node, node.arg, "arg")
            self.generic_visit(node)

    IdentifierVisitor().visit(tree)
    return positions


def exclude_reserved_names(positions: List[Position]) -> List[Position]:
    # Remove attribute names from the list of positions.
    positions = [p for p in positions if p.kind != "attr"]

    # Reserved names (keywords, builtins, and dunder names) must not change.
    reserved = set(keyword.kwlist) | set(dir(builtins))
    positions = [p for p in positions if p.name not in reserved]

    positions = [p for p in positions if not p.name.startswith("__")]

    return positions


def exclude_ranges(source: str, positions: List[Position]) -> List[str]:
    pos_idx = 0
    cur_lineno = 1
    cur_col = 0
    source_idx = 0
    chunks = []

    def getch():
        nonlocal source_idx, cur_lineno, cur_col
        ch = source[source_idx]
        source_idx += 1
        if ch == "\n":
            cur_lineno += 1
            cur_col = 0
        else:
            cur_col += 1
        return ch

    while pos_idx < len(positions):
        pos = positions[pos_idx]
        chunk = ""
        while cur_lineno < pos.lineno or (cur_lineno == pos.lineno and cur_col < pos.col_offset):
            chunk += getch()
        chunks.append(chunk)
        while cur_lineno < pos.end_lineno or (cur_lineno == pos.end_lineno and cur_col < pos.end_col_offset):
            getch()
        pos_idx += 1

    assert source_idx <= len(source)
    if source_idx != len(source):
        chunks.append(source[source_idx:])

    return chunks


# ---------------------------------------------------------------------------
# Identifier rewriting for Python mode
# ---------------------------------------------------------------------------


def _generate_aliases(num_aliases: int, reserved, alphabet: str = string.ascii_lowercase):
    """Generate short, valid Python identifiers.

    Parameters
    ----------
    alphabet:
        A string containing the characters to use when generating names.
        The order of characters determines which identifiers are produced
        first.  By default the standard English alphabet is used, but
        callers may provide a custom ordering to bias the output.
    """

    names = []
    index = 0
    base = len(alphabet)
    while len(names) < num_aliases:
        n = index
        name = ""
        # Convert *index* to a string in the given base using the supplied
        # alphabet.  This effectively counts in base ``base`` and maps each
        # digit to the corresponding character in ``alphabet``.
        while True:
            name = alphabet[n % base] + name
            n //= base
            if n == 0:
                break
        index += 1
        if name not in reserved:
            names.append(name)

    return names


def _shake_list(list, seed):
    rng = random.Random(seed)
    new_list = []
    while list:
        if rng.random() > 0.2 or len(list) == 1:
            new_list += [list[0]]
            list = list[1:]
        else:
            new_list += [list[1]]
            list = [list[0]] + list[2:]
    return new_list


def _shake_alphabet(alphabet, seed):
    return "".join(_shake_list([c for c in alphabet], seed))


def _build_identifier_mapping(source: str, positions, excludes: List[str] = [], seed: int = 0) -> Dict[str, str]:
    """Create a mapping from original identifier to a short alias."""

    # Count occurrences for each identifier while skipping attribute names.
    counts: Counter[str] = Counter()
    for name, _, _, _, _, kind in positions:
        counts[name] += 1

    # Reserved names (keywords, builtins, and dunder names) must not change.
    reserved = set(keyword.kwlist) | set(dir(builtins)) | set(excludes)
    reserved.update(name for name in counts if name.startswith("__"))

    non_identifier_source = "".join(exclude_ranges(source, positions))

    # Build a custom alphabet ordered by letter frequency among the
    # identifiers we actually intend to rename.  Using a tailored alphabet
    # means the shortest aliases start with characters that are more common
    # in the source, potentially improving compression.
    letter_counts: Counter[str] = Counter()
    for ch in non_identifier_source:
        if ch in string.ascii_lowercase:
            letter_counts[ch] += 1

    # Sort letters by decreasing frequency, breaking ties alphabetically so
    # that the result is deterministic even when counts are equal.
    ordered_letters = sorted(
        list(letter_counts.keys()), key=lambda c: (-letter_counts[c], c)
    )
    alphabet = "".join(ordered_letters)

    if seed and seed % 2 == 0:
        alphabet = _shake_alphabet(alphabet, seed)

    orig_names = []
    for name, _ in counts.most_common():
        if name in reserved:
            continue
        orig_names.append(name)

    if seed and seed % 2 == 1:
        orig_names = _shake_list(orig_names, seed)

    mapping: Dict[str, str] = {}
    new_names = _generate_aliases(len(orig_names), reserved, alphabet=alphabet)
    return dict(zip(orig_names, new_names))


def _apply_identifier_mapping(source: str, positions, mapping: Dict[str, str]) -> str:
    """Return *source* with identifiers replaced according to *mapping*.

    The *positions* list is expected to originate from
    :func:`get_identifier_positions`.  Only entries whose name appears in
    ``mapping`` are substituted.  The function works with absolute
    positions, so replacements are applied from left to right without
    affecting subsequent indices.
    """

    if not mapping:
        return source

    # Pre-compute the starting index of each line for fast conversion
    # from (lineno, col) to an absolute character index.
    lines = source.splitlines(keepends=True)
    line_starts = [0]
    for line in lines:
        line_starts.append(line_starts[-1] + len(line))

    def absolute(line: int, col: int) -> int:
        return line_starts[line - 1] + col

    replacements = []
    for name, lineno, col, end_lineno, end_col, kind in positions:
        if name not in mapping or kind == "attr":
            continue
        start = absolute(lineno, col)
        end = absolute(end_lineno, end_col)
        replacements.append((start, end, mapping[name]))

    # Apply replacements in order.
    replacements.sort()
    out = []
    last = 0
    for start, end, repl in replacements:
        out.append(source[last:start])
        out.append(repl)
        last = end
    out.append(source[last:])
    return "".join(out)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def compress(data: Union[str, bytes], is_python: bool) -> bytes:
    """Compress *data* into a zlib-formatted byte stream.

    When ``is_python`` is ``True`` a simple identifier rewriting pass is
    performed before compression.  This pass renames identifiers to short
    aliases in a semantics‑preserving way which often yields better
    compression ratios.
    """

    # Convert to ``str`` if we intend to analyse identifiers.
    if is_python:
        source = data.decode("utf-8") if isinstance(data, bytes) else data
        positions = get_identifier_positions(source)
        positions = exclude_reserved_names(source)
        mapping = _build_identifier_mapping(source, positions)
        source = _apply_identifier_mapping(source, positions, mapping)
        data_bytes = source.encode("utf-8")
    else:
        data_bytes = data.encode("utf-8") if isinstance(data, str) else data

    # ------------------------------------------------------------------
    # LZ77 tokenisation
    # ------------------------------------------------------------------
    tokens: List[Union[int, Match]] = []
    litlen_freq = [0] * 286  # Frequency of literal/length codes
    dist_freq = [0] * 30     # Frequency of distance codes

    i = 0
    while i < len(data_bytes):
        match = _find_match(data_bytes, i)
        if match.length >= 3:
            tokens.append(match)
            lcode, _, _ = _length_code(match.length)
            dcode, _, _ = _distance_code(match.distance)
            litlen_freq[lcode] += 1
            dist_freq[dcode] += 1
            i += match.length
        else:
            literal = data_bytes[i]
            tokens.append(literal)
            litlen_freq[literal] += 1
            i += 1

    # End-of-block marker
    tokens.append(256)
    litlen_freq[256] += 1

    if max(dist_freq) == 0:
        # At least one distance code must be present.
        dist_freq[0] = 1

    # Build Huffman code lengths based on symbol frequencies.
    lit_lengths = _huffman_lengths(litlen_freq)
    dist_lengths = _huffman_lengths(dist_freq)

    out = bytearray()

    # Zlib header: CMF=0x78 (deflate, 32K window), FLG=0x9C (default
    # compression level).  The combination has the required checksum
    # property (CMF*256 + FLG) % 31 == 0.
    out.extend(b"\x78\x9c")

    writer = _BitWriter(out)

    # Block header: BFINAL=1 (single block), BTYPE=10 (dynamic Huffman)
    writer.write(0b101, 3)

    _write_dynamic_header(lit_lengths, dist_lengths, writer)

    lit_codes = _build_codes(lit_lengths)
    dist_codes = _build_codes(dist_lengths)

    for tok in tokens:
        if isinstance(tok, Match):
            code, ebits, eval_ = _length_code(tok.length)
            bits, length = lit_codes[code]
            writer.write(bits, length)
            if ebits:
                writer.write(eval_, ebits)

            dcode, debits, deval = _distance_code(tok.distance)
            dbits, dlen = dist_codes[dcode]
            writer.write(dbits, dlen)
            if debits:
                writer.write(deval, debits)
        else:
            bits, length = lit_codes[tok]
            writer.write(bits, length)

    writer.flush()

    # Adler-32 checksum of uncompressed data, big endian
    checksum = _adler32(data_bytes)
    out.extend(
        (
            (checksum >> 24) & 0xFF,
            (checksum >> 16) & 0xFF,
            (checksum >> 8) & 0xFF,
            checksum & 0xFF,
        )
    )

    return bytes(out)


def map_identifiers(source: str, excludes: List[str], seed: int = 0) -> str:
    """Return *source* with identifiers replaced by short aliases.

    The function analyses Python source code and rewrites identifiers using
    :func:`get_identifier_positions` and the helper routines for building and
    applying an identifier mapping.  Only the modified source code is
    returned; callers interested in the mapping itself can invoke the helper
    functions directly.  ``excludes`` can be used to protect specific
    identifiers from being rewritten.
    """

    # Gather all identifier positions within the source.  This provides the
    # location for every ``ast.Name`` (and a few other constructs) so that the
    # mapping can be applied efficiently later on.
    positions = get_identifier_positions(source)
    positions = exclude_reserved_names(positions)

    # Certain names must never be rewritten because doing so would produce
    # invalid Python code.  Examples are names introduced by import statements
    # or mentioned in ``global``/``nonlocal`` declarations.  The AST stores
    # those names separately, so we scan the tree again to collect them.
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=SyntaxWarning)
        tree = ast.parse(source)
    reserved: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # ``alias.name`` may contain dotted paths ("module.func").  Only the
            # last component becomes a variable name in the current module.  If
            # ``asname`` is present it is the name used in the code.
            for alias in node.names:
                reserved.add(alias.asname or alias.name.split(".")[-1])
        elif isinstance(node, (ast.Global, ast.Nonlocal)):
            reserved.update(node.names)

    # Build a mapping for all identifiers except those explicitly excluded or
    # reserved by the checks above.
    mapping = _build_identifier_mapping(source, positions, excludes + list(reserved), seed=seed)

    # Finally apply the mapping to the original source code.
    mapped_source = _apply_identifier_mapping(source, positions, mapping)
    return mapped_source


if __name__ == "__main__":
    import sys
    import zlib
    import zopfli.zlib

    if len(sys.argv) == 1:
        sample = "if __name__ == '__main__':"
        # Sanity check: compression round trip without Python specific tweaks.
        assert zlib.decompress(compress(sample, False)) == sample.encode()

        assert map_identifiers("def ppp(g):return len(g)") == "def b(a):return len(a)"
    elif sys.argv[1] == "--map":
        source = open(sys.argv[2]).read()
        print(map_identifiers(source, excludes=["p"]))
    else:
        stats = {}

        def add_stat(name, value):
            print(f"{name}: {value}")
            if name not in stats:
                stats[name] = []
            stats[name].append(value)

        for arg in sys.argv[1:]:
            text = open(arg, "rb").read()
            add_stat("orig", len(text))
            add_stat("zlib", len(zlib.compress(text, 9)))
            add_stat(
                "zopfli",
                len(
                    zopfli.zlib.compress(
                        text,
                        numiterations=1000,
                        blocksplitting=True,
                        blocksplittinglast=False,
                        blocksplittingmax=100,
                    )
                ),
            )

            if arg.endswith(".py"):
                # For Python files, show identifier list and run both modes.
                source = text.decode("utf-8")
                id_pos = get_identifier_positions(source)
                id_pos = exclude_reserved_names(id_pos)
                names = sorted({name for name, *_ in id_pos})
                print(f"{arg} identifiers: {', '.join(names)}")
                add_stat("mine", len(compress(text, False)))
                add_stat("mine-py", len(compress(text, True)))
            else:
                add_stat("mine", len(compress(text, False)))

        for name, values in stats.items():
            print(f"{name} avg: {sum(values) / len(values)}")
