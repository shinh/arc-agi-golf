def p(g):
    # place shapes touching edges, else near center
    d={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):d[v]=d.get(v,[])+[(i,j)]
    bg=max(d,key=lambda k:len(d[k]));d.pop(bg)
    if not d:return[[bg]]
    H=W=0
    for c,v in d.items():
        xs,ys=zip(*v);mi=min(xs);mj=min(ys)
        s=[(x-mi,y-mj)for x,y in v]
        a=max(xs)-mi+1;b=max(ys)-mj+1
        d[c]=s,a,b
        H,W=max(H,a),max(W,b)
    O=[[bg]*W for _ in range(H)]
    for c,(s,a,b) in d.items():
        *_,bi,bj=max((sum(i+di in(0,H-1)or j+dj in(0,W-1)for di,dj in s),-abs(i+a//2-H//2)-abs(j+b//2-W//2),i,j)for i in range(H-a+1)for j in range(W-b+1))
        for di,dj in s:O[bi+di][bj+dj]=c
    return O

