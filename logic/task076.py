def p(g):
    h=len(g);w=len(g[0]);S=set();O=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 or (i,j) in S:continue
            q=[(i,j)];S.add((i,j));o=[]
            while q:
                x,y=q.pop();o+=[(g[x][y],x,y)]
                for dx in(-1,0,1):
                    for dy in(-1,0,1):
                        if dx or dy:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and g[nx][ny] and (nx,ny)not in S:
                                S.add((nx,ny));q+=[(nx,ny)]
            O+=[o]
    O.sort(key=len,reverse=True);b=O[0]
    P={v for o in O[1:] for v,_,_ in o}
    sub=[(v,r,c) for v,r,c in b if v in P]
    if not sub:return [r[:] for r in g]
    br=min(r for _,r,_ in b);bc=min(c for _,_,c in b)
    h0=max(r for _,r,_ in b)-br+1;w0=max(c for _,_,c in b)-bc+1
    B=[(r-br,c-bc,v) for v,r,c in b]
    S=[(r-br,c-bc,v) for v,r,c in sub]
    def T(L,t):
        R=[]
        for r,c,v in L:
            if t==1:r,c=c,h0-1-r
            elif t==2:r,c=h0-1-r,w0-1-c
            elif t==3:r,c=w0-1-c,r
            elif t==4:r,c=h0-1-r,c
            elif t==5:r,c=r,w0-1-c
            elif t==6:r,c=c,r
            elif t==7:r,c=w0-1-c,h0-1-r
            R+=[(r,c,v)]
        return R
    G=[r[:] for r in g]
    for t in range(8):
        F=T(B,t);P=T(S,t)
        mr=min(r for r,_,_ in P);mc=min(c for _,c,_ in P)
        F=[(r-mr,c-mc,v) for r,c,v in F];P=[(r-mr,c-mc,v) for r,c,v in P]
        hp=max(r for r,_,_ in P)+1;wp=max(c for _,c,_ in P)+1
        for i in range(h-hp+1):
            for j in range(w-wp+1):
                if all(g[i+r][j+c]==v for r,c,v in P):
                    for r,c,v in F:
                        ii=i+r;jj=j+c
                        if 0<=ii<h and 0<=jj<w:G[ii][jj]=v
    return G
