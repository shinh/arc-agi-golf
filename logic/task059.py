def p(g):
    # paint densest 3x3 block with its color
    r=0,1,2;s=0,4,8
    h=[(len(t:=[a for i in r for j in r if (a:=g[y+i][x+j])%5]),sum(t[:1]),y,x)for y in s for x in s]
    m=max(h)[0]
    for n,u,y,x in h:
        for i in r:g[y+i][x:x+3]=[(n==m)*u]*3
    return g
