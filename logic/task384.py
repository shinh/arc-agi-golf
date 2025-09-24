# crop bbox of nonzeros and double size
p=lambda g:[[*sum(zip(r,r),())]for r in zip(*filter(any,zip(*g)))if any(r)for _ in'__']
