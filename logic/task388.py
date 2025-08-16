# fill columns with 8 then tile 2x2
p=lambda g:[[k[0]or-any(k)&8for k in zip(r,*g)]*2 for r in g]*2
