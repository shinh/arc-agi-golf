def p(g):
    h=len(g);w=len(g[0])
    s={(i,j)for i in range(h)for j in range(w)if g[i][j]};m=[];C=set()
    while s:
        q=[s.pop()];o=[]
        while q:
            x,y=q.pop();o+=(g[x][y],x,y),
            for a in(-1,0,1):
                for b in(-1,0,1):
                    if a|b:
                        p=x+a,y+b
                        if p in s:s.remove(p);q+=p,
        if len(o)>len(m):m,o=o,m
        C|={v for v,_,_ in o}
    B=[(r,c,v)for v,r,c in m]
    rs,cs,_=zip(*B);br=min(rs);bc=min(cs);H=max(rs)-br+1;W=max(cs)-bc+1
    B=[(r-br,c-bc,v)for r,c,v in B]
    S=[t for t in B if t[2]in C]
    if not S:return g
    G=[x[:]for x in g];col=S[0][2];pos=[(i,j)for i in range(h)for j in range(w)if g[i][j]==col]
    for t in range(8):
        s=t&1;H0,W0=(W,H)if s else(H,W);F=[];P=[]
        for R,L in (F,B),(P,S):
            for r,c,v in L:
                if s:r,c=c,r
                if t&2:r=H0-1-r
                if t&4:c=W0-1-c
                R+=[(r,c,v)]
        r0,c0,_=P[0]
        for i,j in pos:
            d=i-r0;j_=j-c0
            if all(0<=d+r<h and 0<=j_+c<w and g[d+r][j_+c]==v for r,c,v in P):
                for r,c,v in F:
                    x=d+r;y=j_+c
                    if 0<=x<h and 0<=y<w:G[x][y]=v
    return G
