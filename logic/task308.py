def p(g):
    d={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):d[v]=d.get(v,[])+[(i,j)]
    bg=max(d,key=lambda k:len(d[k]))
    if len(d)<2:return[[bg]]
    d.pop(bg)
    H=W=0
    for c in d:
        v=d[c];mi=min(i for i,_ in v);mj=min(j for _,j in v)
        sh=[(i-mi,j-mj)for i,j in v]
        a=max(i for i,_ in sh)+1;b=max(j for _,j in sh)+1
        d[c]=sh,a,b
        H=max(H,a);W=max(W,b)
    O=[[bg]*W for _ in range(H)];M=max(H,W)*2
    for c,(sh,a,b) in d.items():
        h=a//2;w=b//2
        best,bi,bj=max((M*sum(i+di in (0,H-1) or j+dj in (0,W-1) for di,dj in sh)-abs(i+h-H//2)-abs(j+w-W//2),i,j) for i in range(H-a+1) for j in range(W-b+1))
        for di,dj in sh:O[bi+di][bj+dj]=c
    return O
