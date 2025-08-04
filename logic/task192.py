def p(g):
    h=len(g);w=len(g[0]);c=[0]*10
    for r in g:
        for v in r:c[v]+=1
    b=max(range(1,10),key=c.__getitem__)
    for y in range(h):
        for x in range(w):
            v=g[y][x]
            if v and v!=b:
                U=y and g[y-1][x]==b;D=y<h-1 and g[y+1][x]==b
                L=x and g[y][x-1]==b;R=x<w-1 and g[y][x+1]==b
                n=U+D+L+R
                g[y][x]=b if n>2 or n==2 and not((U and D) or (L and R)) else 0
    return g
