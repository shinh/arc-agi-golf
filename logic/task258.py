# fill middle between nonzero neighbors
p=lambda g:[r[:1]+[a&c and 2or b for a,b,c in zip(r,r[1:],r[2:])]+r[-1:]for r in g]
