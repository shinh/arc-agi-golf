# fill columns with 8 then tile 2x2
p=lambda g:[[c or 8*any(t)for c,t in zip(r,zip(*g))]*2 for r in g]*2
