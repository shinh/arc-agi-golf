def p(g):
    h=len(g);w=len(g[0])
    s={(i,j)for i in range(h)for j in range(w)if g[i][j]};m=[];C=set()
    while s:
        q=[s.pop()];o=[]
        while q:
            x,y=q.pop();o+=(x,y),
            for a in(-1,0,1):
                for b in(-1,0,1):
                    if a|b and(p:=(x+a,y+b))in s:s.remove(p);q+=p,
        if len(o)>len(m):m,o=o,m
        C|={g[x][y]for x,y in o}
    rs,cs=zip(*m);a=min(rs);b=min(cs);H=max(rs)-a+1;W=max(cs)-b+1
    B=[(r-a,c-b,g[r][c])for r,c in m]
    I=[i for i,(_,_,v)in enumerate(B)if v in C]
    if not I:return g
    G=[*map(list,g)];Q=[(i,j)for i in range(h)for j in range(w)if g[i][j]==B[I[0]][2]]
    for t in range(8):
        h0,w0=(W,H)if t&1 else(H,W);F=[]
        for r,c,k in B:
            if t&1:r,c=c,r
            if t&2:r=h0-1-r
            if t&4:c=w0-1-c
            F+=(r,c,k),
        a,b,_=F[I[0]]
        for i,j in Q:
            i-=a;j-=b
            if all(0<=i+r<h>0<=j+c<w and g[i+r][j+c]==k for n in I for r,c,k in (F[n],)):
                for r,c,k in F:
                    x,y=i+r,j+c
                    if 0<=x<h>0<=y<w:G[x][y]=k
    return G
