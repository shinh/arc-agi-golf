def p(g):
    h=len(g);w=len(g[0])
    bg=g[0][0]
    cols={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v!=bg: cols.setdefault(v,[]).append((i,j))
    (_,S),(c2,B)=sorted(cols.items(),key=lambda kv:-len(kv[1]))[:2]
    S=set(S);B=set(B);s=0
    while {(i+s,j+s) for i,j in S}&S:s+=1
    d=max([(-1,-1),(-1,1),(1,-1),(1,1)],key=lambda d:len({(i+d[0]*s,j+d[1]*s) for i,j in S}&B))
    out=[r[:] for r in g];m=max(h,w)
    for k in range(1,m+1):
        di,dj=d[0]*s*k,d[1]*s*k
        for i,j in S:
            x,y=i+di,j+dj
            if 0<=x<h and 0<=y<w: out[x][y]=c2
    return out
