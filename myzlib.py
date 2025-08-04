"""Minimal zlib compression implementation.

This module provides a :func:`compress` function that mirrors
``zlib.compress`` but avoids using the :mod:`zlib` module altogether.

The goal here is not to offer a fast or fully–featured compressor; it
simply produces byte streams that are understood by ``zlib.decompress``.
The implementation uses an "uncompressed" DEFLATE block which stores the
original data verbatim and appends an Adler‑32 checksum.  This is enough
for correctness while keeping the code straightforward.

The function accepts either ``bytes`` or ``str`` (which will be encoded
using UTF‑8) and always returns ``bytes``.
"""

from typing import Union


def _adler32(data: bytes) -> int:
    """Compute the Adler-32 checksum.

    The checksum is defined by two sums A and B over all bytes in
    ``data``.  Each sum is kept modulo ``65521`` (the largest prime number
    less than ``2**16``) to avoid overflow.  The final checksum is
    ``(B << 16) | A``.
    """

    MOD_ADLER = 65521
    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a


def compress(data: Union[str, bytes]) -> bytes:
    """Return a zlib-formatted byte string representing ``data``.

    The implementation uses a single uncompressed DEFLATE block.  While
    this does not reduce the size of the input, it creates a valid zlib
    stream that can be decompressed by standard tools.

    Parameters
    ----------
    data:
        The data to "compress".  ``str`` inputs are encoded using
        UTF‑8.
    """

    # Accept both ``str`` and ``bytes`` inputs for convenience.
    if isinstance(data, str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data

    # ``bytearray`` is convenient for incremental construction.
    out = bytearray()

    # ------------------------------------------------------------------
    # Zlib header: CMF and FLG bytes.
    #  CMF: 0x78 = 0b01111000 -> Compression method 8 (DEFLATE) and a
    #       32K window size.
    #  FLG: 0x01 indicates no compression / fastest algorithm.  The
    #       combination 0x78 0x01 has a check bits value that makes the
    #       16-bit header a multiple of 31, as required by RFC 1950.
    # ------------------------------------------------------------------
    out.extend(b"\x78\x01")

    # ------------------------------------------------------------------
    # DEFLATE block: we emit a single "stored" (uncompressed) block.
    # The block format is:
    #   [BFINAL BTYPE] [LEN (16-bit)] [NLEN (16-bit)] [DATA]
    # Since this block is the only one, BFINAL=1 and BTYPE=00.
    # ``LEN`` is the number of bytes in DATA and ``NLEN`` is its one's
    # complement.
    # ------------------------------------------------------------------
    block = data_bytes
    length = len(block)

    if length > 0xFFFF:
        raise ValueError("Data too large for single uncompressed block")

    # Block header byte: BFINAL=1 (last block), BTYPE=00 (stored block).
    out.append(0x01)

    # Little-endian length and one's complement.
    out.extend((length & 0xFF, (length >> 8) & 0xFF))
    nlen = (~length) & 0xFFFF
    out.extend((nlen & 0xFF, (nlen >> 8) & 0xFF))

    # Actual data payload.
    out.extend(block)

    # Append Adler-32 checksum of the uncompressed data, big-endian.
    checksum = _adler32(block)
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
    import zlib
    orig = 'if __name__ == "__main__":'
    decompressed = zlib.decompress(compress(orig)).decode("utf-8")
    assert decompressed == orig
