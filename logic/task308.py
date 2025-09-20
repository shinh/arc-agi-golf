def p(g):# place shapes touching edges, else near center
    f=sum(g,[]);bg=max(f,key=f.count);q={*f}-{bg}
    if not q:return[[bg]]
    H=W=0;S=[]
    for c in q:
        v=[(y,x)for y,r in enumerate(g)for x,t in enumerate(r)if t==c]
        ys,xs=zip(*v);a=min(ys);b=min(xs);s=[(y-a,x-b)for y,x in v];h=max(ys)-a+1;w=max(xs)-b+1
        S+=[(c,s,h,w)];H=max(H,h);W=max(W,w)
    O=[[bg]*W for _ in[0]*H]
    for c,s,h,w in S:
        y,x=max((sum(y+i in(0,H-1)or x+j in(0,W-1)for i,j in s),-abs(H-h-2*y)-abs(W-w-2*x),y,x)for y in range(H-h+1)for x in range(W-w+1))[2:]
        for i,j in s:O[y+i][x+j]=c
    return O
