def p(g):
    d={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):d.setdefault(v,[]).append((i,j))
    bg=max(d,key=lambda k:len(d[k]))
    if len(d)==1:return [[bg]]
    d.pop(bg)
    H=W=0
    for c,cells in d.items():
        mi=min(i for i,_ in cells);mj=min(j for _,j in cells)
        sh=[(i-mi,j-mj)for i,j in cells]
        ph=max(i for i,_ in sh)+1;pw=max(j for _,j in sh)+1
        d[c]=sh,ph,pw
        H=max(H,ph);W=max(W,pw)
    O=[[bg]*W for _ in range(H)];M=max(H,W);ch,cw=H//2,W//2
    for c,(sh,ph,pw) in d.items():
        best=-10**9
        for i in range(H):
            for j in range(W):
                s=2*M*sum(0<=i+di<H and 0<=j+dj<W and (i+di in (0,H-1) or j+dj in (0,W-1)) for di,dj in sh)-abs(i+ph//2-ch)-abs(j+pw//2-cw)
                if s>best:best=s;bi=i;bj=j
        for di,dj in sh:
            ni=bi+di;nj=bj+dj
            if 0<=ni<H and 0<=nj<W:O[ni][nj]=c
    return O

