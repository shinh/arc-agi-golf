def p(g):
    h=len(g);w=len(g[0])
    cnt={}
    for r in g:
        for v in r:cnt[v]=cnt.get(v,0)+1
    bg=max(cnt,key=cnt.get)
    seen=set();pcs=[];mh=mw=0
    for i in range(h):
        for j in range(w):
            if g[i][j]==bg or (i,j) in seen:continue
            c=g[i][j];q=[(i,j)];seen.add((i,j));cells=[]
            while q:
                x,y=q.pop(0);cells.append((x,y))
                for dx in(-1,0,1):
                    for dy in(-1,0,1):
                        if dx or dy:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and g[nx][ny]==c and (nx,ny)not in seen:
                                seen.add((nx,ny));q.append((nx,ny))
            mi=min(x for x,_ in cells);mj=min(y for _,y in cells)
            sh=[(x-mi,y-mj)for x,y in cells]
            pcs.append((c,sh))
            mh=max(mh,max(x for x,_ in sh)+1)
            mw=max(mw,max(y for _,y in sh)+1)
    if not pcs:return [[bg]]
    freq={}
    for c,sh in pcs:
        k=(c,tuple(sorted(sh)))
        freq[k]=freq.get(k,0)+1
    c,sh=max(freq,key=freq.get)
    o=[[bg]*mw for _ in range(mh)]
    for x,y in sh:o[x][y]=c
    return o

