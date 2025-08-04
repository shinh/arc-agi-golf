"""A tiny (and slow) DEFLATE encoder.

This module implements just enough of the DEFLATE format to create
zlib-compatible compressed streams.  It is intentionally written for
clarity rather than performance and supports only a single block using
*dynamically generated* Huffman code tables as described in RFC 1951.

The :func:`compress` function accepts ``bytes`` or ``str`` and returns a
``bytes`` object which can be fed to :func:`zlib.decompress`.
"""

from __future__ import annotations

from dataclasses import dataclass
import heapq
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
            heap.append((freq, sym, sym))
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


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def compress(data: Union[str, bytes]) -> bytes:
    """Compress *data* into a zlib-formatted byte stream.

    The implementation is intentionally straightforward and supports only
    a single DEFLATE block using dynamically generated Huffman tables.
    Despite its simplicity it produces output compatible with
    :func:`zlib.decompress` and achieves respectable compression ratios
    for typical text inputs.
    """

    # Normalise the input to a ``bytes`` object.
    if isinstance(data, str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data

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


if __name__ == "__main__":
    import sys
    import zlib
    import zopfli.zlib

    if len(sys.argv) == 1:
        sample = "if __name__ == '__main__':"
        assert zlib.decompress(compress(sample)) == sample.encode()
    else:
        text = open(sys.argv[1], "rb").read()
        print("orig:", len(text))
        print("zlib:", len(zlib.compress(text, 9)))
        print("zopfli:", len(zopfli.zlib.compress(
            text,
            numiterations=1000,
            blocksplitting=True,
            blocksplittinglast=False,
            blocksplittingmax=100
        )))
        print("mine:", len(compress(text)))
