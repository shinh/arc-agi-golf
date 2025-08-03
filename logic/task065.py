def p(g):
    s=sum(g,[]);m=len(g);n=m//2
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if s.count(c)<2:
                a=range(n)if y<n else range(n+1,m)
                b=range(n)if x<n else range(n+1,m)
                return[[g[i][j]for j in b]for i in a]
