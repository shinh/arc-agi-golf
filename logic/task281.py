def p(g):
    # spread color
    for o in[0]*4:
        if (e:=[r.index(8)for r in g if 8 in r]):
            e=e[0]
            for r in g:
                f=n=0
                for x,c in enumerate(r):
                    if c:f<1and(f:=c)or n<1and(n:=c)
                    elif n and x<e:r[x-1:e+1]=[n]*(e-x+1)+[f];n=0
        g=[*map(list,zip(*g[::-1]))]
    return g
