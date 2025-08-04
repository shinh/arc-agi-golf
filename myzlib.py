"""A tiny (and slow) DEFLATE encoder.

This module implements just enough of the DEFLATE format to create
zlib-compatible compressed streams.  It is intentionally written for
clarity rather than performance and supports only a single block using
the *fixed Huffman* code tables defined in RFC 1951.

The :func:`compress` function accepts ``bytes`` or ``str`` and returns a
``bytes`` object which can be fed to :func:`zlib.decompress`.
"""

from __future__ import annotations

from dataclasses import dataclass
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


# Build the fixed Huffman tables used by this encoder.
# Literal/length codes 0-287
_lit_lengths = [0] * 288
_lit_lengths[:144] = [8] * 144
_lit_lengths[144:256] = [9] * 112
_lit_lengths[256:280] = [7] * 24
_lit_lengths[280:] = [8] * 8
FIXED_LITERAL_CODES = _build_codes(_lit_lengths)

# Distance codes 0-31, all 5 bits
_dist_lengths = [5] * 32
FIXED_DISTANCE_CODES = _build_codes(_dist_lengths)

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

    The resulting byte string is compatible with :func:`zlib.decompress`.
    Only the most common features of DEFLATE are implemented: a single
    block using fixed Huffman codes.  The algorithm is intentionally
    simple and therefore quite slow, but it does achieve real compression
    for typical text inputs.
    """

    if isinstance(data, str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data

    out = bytearray()

    # Zlib header: CMF=0x78 (deflate, 32K window), FLG=0x9C (default
    # compression level).  The combination has the required checksum
    # property (CMF*256 + FLG) % 31 == 0.
    out.extend(b"\x78\x9c")

    writer = _BitWriter(out)

    # Write a single block header.  The three bits are, in order:
    #   BFINAL = 1  (this is the last block)
    #   BTYPE  = 01 (fixed Huffman codes)
    writer.write(0b011, 3)

    i = 0
    while i < len(data_bytes):
        match = _find_match(data_bytes, i)
        if match.length >= 3:
            # Encode length and distance pair
            code, ebits, eval_ = _length_code(match.length)
            bits, length = FIXED_LITERAL_CODES[code]
            writer.write(bits, length)
            if ebits:
                writer.write(eval_, ebits)

            dcode, debits, deval = _distance_code(match.distance)
            dbits, dlen = FIXED_DISTANCE_CODES[dcode]
            writer.write(dbits, dlen)
            if debits:
                writer.write(deval, debits)

            i += match.length
        else:
            # Emit literal byte
            literal = data_bytes[i]
            bits, length = FIXED_LITERAL_CODES[literal]
            writer.write(bits, length)
            i += 1

    # End-of-block marker
    eob_bits, eob_len = FIXED_LITERAL_CODES[256]
    writer.write(eob_bits, eob_len)
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

    if len(sys.argv) == 1:
        sample = "if __name__ == '__main__':"
        assert zlib.decompress(compress(sample)) == sample.encode()
    else:
        text = open(sys.argv[1], "rb").read()
        print("orig:", len(text))
        print("zlib:", len(zlib.compress(text, 9)))
        print("mine:", len(compress(text)))
