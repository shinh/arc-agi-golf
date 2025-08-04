def p(g):
    def r(x):return [list(y)for y in zip(*x[::-1])]
    n=0
    while True:
        c=[(i,j)for i,rw in enumerate(g)for j,v in enumerate(rw)if v==2]
        if{c[0][0]}=={i for i,_ in c} and min(j for _,j in c)==0:break
        g=r(g);n+=1
    h=len(g);w=len(g[0]);r0=c[0][0];L=len(c)
    for i in range(r0):
        for j in range(L+r0-i):g[i][j]=3
    for k in range(1,L):
        y=r0+k
        if y<h:
            for j in range(L-k):g[y][j]=1
    for _ in range(-n%4):g=r(g)
    return g
