def p(g):
    d={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):d.setdefault(v,[]).append((i,j))
    bg=max(d,key=lambda k:len(d[k]))
    if len(d)==1:return [[bg]]
    d.pop(bg)
    H=W=0
    for c in d:
        mi=min(i for i,_ in d[c]);mj=min(j for _,j in d[c])
        sh=[(i-mi,j-mj)for i,j in d[c]]
        d[c]=sh
        H=max(H,max(i for i,_ in sh)+1);W=max(W,max(j for _,j in sh)+1)
    O=[[bg]*W for _ in range(H)]
    for c,sh in d.items():
        h=(max(i for i,_ in sh)+1)//2;w=(max(j for _,j in sh)+1)//2
        best,bi,bj=max((2*max(H,W)*sum(0<=i+di<H and 0<=j+dj<W and (i+di in (0,H-1) or j+dj in (0,W-1)) for di,dj in sh)-abs(i+h-H//2)-abs(j+w-W//2),i,j) for i in range(H) for j in range(W))
        for di,dj in sh:0<=bi+di<H and 0<=bj+dj<W and O[bi+di].__setitem__(bj+dj,c)
    return O

