def p(g):
    h,w=len(g),len(g[0])
    for bh in range(1,h):
        if len(set(g[bh]))==1:break
    for bw in range(1,w):
        if len({g[i][bw] for i in range(h)})==1:break
    sr,sc=bh+1,bw+1
    B=[[g[r][c]for c in range(0,w,sc)]for r in range(0,h,sr)]
    H,W=len(B),len(B[0])
    flat=sum(B,[]);bg=max(set(flat),key=flat.count)
    seen=[[0]*W for _ in range(H)];objs=[]
    for i in range(H):
        for j in range(W):
            if seen[i][j] or B[i][j]==bg:continue
            q=[(i,j)];seen[i][j]=1;o=[]
            while q:
                y,x=q.pop();o.append((y,x,B[y][x]))
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and B[ny][nx]!=bg:
                        seen[ny][nx]=1;q.append((ny,nx))
            objs.append(o)
    if not objs:return g
    obj=max(objs,key=lambda o:len({c for _,_,c in o}))
    oth=[o for o in objs if o is not obj]
    cols=[c for _,_,c in obj]
    t=oth[0][0][2] if oth else None
    c=t if t in cols else min(set(cols),key=cols.count)
    mn=min(y for y,_,_ in obj);ml=min(x for _,x,_ in obj)
    pat=[(col,y-mn,x-ml)for y,x,col in obj]
    ay,ax=min((y,x) for col,y,x in pat if col==c)
    pat=[(col,y-ay,x-ax)for col,y,x in pat]
    tgt=[];seen=[[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if seen[i][j] or B[i][j]!=c:continue
            q=[(i,j)];seen[i][j]=1;ys=[i];xs=[j]
            while q:
                y,x=q.pop()
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and B[ny][nx]==c:
                        seen[ny][nx]=1;q.append((ny,nx));ys.append(ny);xs.append(nx)
            tgt.append((min(ys),min(xs)))
    for ty,tx in tgt:
        for col,dy,dx in pat:
            y,x=ty+dy,tx+dx
            if 0<=y<H and 0<=x<W:B[y][x]=col
    out=[r[:]for r in g]
    for bi in range(H):
        for bj in range(W):
            v=B[bi][bj];r0=bi*sr;c0=bj*sc
            for i in range(bh):
                for j in range(bw):out[r0+i][c0+j]=v
    return out
