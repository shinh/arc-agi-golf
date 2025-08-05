def p(g):
    d={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):d[v]=d.get(v,[])+[(i,j)]
    bg=max(d,key=lambda k:len(d[k]));d.pop(bg)
    if not d:return[[bg]]
    H=W=0
    for c in d:
        v=d[c];mi=min(i for i,_ in v);mj=min(j for _,j in v)
        s=[(i-mi,j-mj)for i,j in v]
        a=max(i for i,_ in s)+1;b=max(j for _,j in s)+1
        d[c]=s,a,b
        H=max(H,a);W=max(W,b)
    O=[[bg]*W for _ in range(H)]
    for c,(s,a,b) in d.items():
        _,bi,bj=max((max(H,W)*2*sum(i+di in (0,H-1) or j+dj in (0,W-1) for di,dj in s)-abs(i+a//2-H//2)-abs(j+b//2-W//2),i,j) for i in range(H-a+1) for j in range(W-b+1))
        for di,dj in s:O[bi+di][bj+dj]=c
    return O
