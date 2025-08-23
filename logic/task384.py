# crop bbox of nonzeros and double size
p=lambda g:[[v for v in r for _ in(0,0)]for r in zip(*filter(any,zip(*g)))if any(r)for _ in(0,0)]
