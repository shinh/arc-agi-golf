def p(g):# place shapes touching edges, else near center
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):d[v]=d.get(v,[])+[(y,x)]
    bg=max(d,key=lambda k:len(d[k]));del d[bg]
    if not d:return[[bg]]
    H=W=0
    for c,v in d.items():
        xs,ys=zip(*v);mi=min(xs);mj=min(ys);s=[(x-mi,y-mj)for x,y in v];a=max(xs)-mi+1;b=max(ys)-mj+1;d[c]=s,a,b;H=max(H,a);W=max(W,b)
    O=[[bg]*W for _ in[0]*H]
    for c,(s,a,b) in d.items():
        *_,y,x=max((sum(y+i in(0,H-1)or x+j in(0,W-1)for i,j in s),-abs(H-a-2*y)-abs(W-b-2*x),y,x)for y in range(H-a+1)for x in range(W-b+1))
        for i,j in s:O[y+i][x+j]=c
    return O

