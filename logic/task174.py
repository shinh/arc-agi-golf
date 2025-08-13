def p(o):
    r=[]
    for c in set(sum(o,[]))-{0}:
        g=o
        for i in range(80):
            g=[*map(list,zip(*g[c not in g[0]:][::-1]))]
        if all(r==r[::-1]for r in g):
            return g
