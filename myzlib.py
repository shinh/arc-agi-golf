def compress(data):
    # Implement this without zlib!
    pass


if __name__ == "__main__":
    import zlib
    orig = 'if __name__ == "__main__":'
    assert zlib.decompress(compress(orig)) == orig
