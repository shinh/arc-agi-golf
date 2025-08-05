def p(g):
    h=len(g);w=len(g[0]);m=b=n=e=0
    for y in range(h-2):
        for x in range(w-2):
            s=[g[y+i][x+j] for i in range(3) for j in range(3)]
            c=s.count(1);d=s.count(8)
            if c>m or c==m and d>e:m=c;e=d;b=y;n=x
    return [r[n:n+3] for r in g[b:b+3]]
