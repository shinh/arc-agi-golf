def p(g):
    h=len(g);w=len(g[0])
    s={(i,j)for i in range(h)for j in range(w)if g[i][j]};m=[];C=set()
    while s:
        q=[s.pop()];o=[]
        while q:
            x,y=q.pop();o+=(x,y,g[x][y]),
            for a in(-1,0,1):
                for b in(-1,0,1):
                    if a|b and(p:=(x+a,y+b))in s:s.remove(p);q+=p,
        if len(o)>len(m):m,o=o,m
        C|={v for _,_,v in o}
    rs,cs,_=zip(*m);a=min(rs);b=min(cs);H=max(rs)-a+1;W=max(cs)-b+1
    B=[(r-a,c-b,v)for r,c,v in m]
    I=[i for i,(_,_,v)in enumerate(B)if v in C]
    if not I:return g
    G=[x[:]for x in g];v=B[I[0]][2];Q=[(i,j)for i in range(h)for j in range(w)if g[i][j]==v]
    for t in range(8):
        s=t&1;H0,W0=(W,H)if s else(H,W);F=[]
        for r,c,k in B:
            if s:r,c=c,r
            if t&2:r=H0-1-r
            if t&4:c=W0-1-c
            F+=[(r,c,k)]
        P=[F[i]for i in I];r0,c0,_=P[0]
        for i,j in Q:
            d=i-r0;j-=c0
            if all(0<=d+r<h>0<=j+c<w and g[d+r][j+c]==k for r,c,k in P):
                for r,c,k in F:
                    x=d+r;y=j+c
                    if 0<=x<h>0<=y<w:G[x][y]=k
    return G
