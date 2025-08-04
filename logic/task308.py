def p(g):
    h=len(g);w=len(g[0])
    cnt={}
    for r in g:
        for v in r:cnt[v]=cnt.get(v,0)+1
    bg=max(cnt,key=cnt.get)
    groups={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v!=bg:groups.setdefault(v,[]).append((i,j))
    if not groups:return [[bg]]
    patches={};H=W=0
    for c,cells in groups.items():
        mi=min(i for i,_ in cells);mj=min(j for _,j in cells)
        sh=[(i-mi,j-mj)for i,j in cells]
        patches[c]=sh
        H=max(H,max(i for i,_ in sh)+1)
        W=max(W,max(j for _,j in sh)+1)
    O=[[bg]*W for _ in range(H)]
    M=max(H,W);ctr=(H//2,W//2)
    for c,sh in patches.items():
        ph=max(i for i,_ in sh)+1;pw=max(j for _,j in sh)+1
        best=(None,-10**9)
        for i in range(H):
            for j in range(W):
                b=sum(0<=i+di<H and 0<=j+dj<W and (i+di in (0,H-1) or j+dj in (0,W-1)) for di,dj in sh)
                d=abs(i+ph//2-ctr[0])+abs(j+pw//2-ctr[1])
                s=2*M*b-d
                if s>best[1]:best=((i,j),s)
        bi,bj=best[0]
        for di,dj in sh:
            ni, nj=bi+di,bj+dj
            if 0<=ni<H and 0<=nj<W:O[ni][nj]=c
    return O

