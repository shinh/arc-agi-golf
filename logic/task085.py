def p(g):
    o=[r for r in g]
    for y in range(1,len(g)-1):
        a,b,c=g[y-1],g[y],g[y+1]
        if a==b==c and any(b):
            k=next(v for v in b if v)
            s=b.index(k);e=len(b)-1-b[::-1].index(k)
            for x in range(s,e+1):o[y][x]=k if (x-s)%2==0 else 0
    return o
