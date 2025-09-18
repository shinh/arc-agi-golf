# crop nonzero rows/cols then double
p=lambda g:[r*2 for r in zip(*filter(any,zip(*g)))if sum(r)]

