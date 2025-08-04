def p(g):
    h=len(g);w=len(g[0]);V=set();C=[]
    for i in range(h):
        for j in range(w):
            if g[i][j] and (i,j)not in V:
                q=[(i,j)];V.add((i,j));o=[]
                while q:
                    x,y=q.pop();o+=[(g[x][y],x,y)]
                    for a in(-1,0,1):
                        for b in(-1,0,1):
                            if a or b:
                                nx,ny=x+a,y+b
                                if 0<=nx<h and 0<=ny<w and g[nx][ny] and (nx,ny)not in V:
                                    V.add((nx,ny));q+=[(nx,ny)]
                C+=[o]
    C.sort(key=len,reverse=True);b=C[0]
    P={v for o in C[1:] for v,_,_ in o}
    sub=[(v,r,c) for v,r,c in b if v in P]
    if not sub:return [r[:] for r in g]
    rs=[r for _,r,_ in b];cs=[c for _,_,c in b];br=min(rs);bc=min(cs);H=max(rs)-br+1;W=max(cs)-bc+1
    B=[(r-br,c-bc,v) for v,r,c in b];S=[(r-br,c-bc,v) for v,r,c in sub]
    G=[r[:] for r in g]
    for t in range(8):
        s=t&1;H0=W if s else H;W0=H if s else W;F=[];P=[]
        for L,R in ((B,F),(S,P)):
            for r,c,v in L:
                if s:r,c=c,r
                if t&2:r=H0-1-r
                if t&4:c=W0-1-c
                R+=[(r,c,v)]
        rs=[r for r,_,_ in P];cs=[c for _,c,_ in P];mr=min(rs);mc=min(cs)
        F=[(r-mr,c-mc,v) for r,c,v in F];P=[(r-mr,c-mc,v) for r,c,v in P]
        hp=max(rs)-mr+1;wp=max(cs)-mc+1
        for i in range(h-hp+1):
            for j in range(w-wp+1):
                if all(g[i+r][j+c]==v for r,c,v in P):
                    for r,c,v in F:
                        x=i+r;y=j+c
                        if 0<=x<h and 0<=y<w:G[x][y]=v
    return G
