def p(g):
    for _ in "0000":
        g=[r for r in g if any(r)]
        g=[list(r)for r in zip(*g)]
    u=[]
    for r in g:
        if r not in u:u+=r,
    g=[list(r)for r in zip(*u)]
    u=[]
    for r in g:
        if r not in u:u+=r,
    return [list(r)for r in zip(*u)]
