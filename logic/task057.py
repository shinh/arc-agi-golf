# crop nonzero rows/cols then double
p=lambda g:[r+r for r in zip(*filter(any,zip(*g)))if any(r)]

