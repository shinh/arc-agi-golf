def p(g):
    h=len(g);w=len(g[0]);bg=0
    c=[(i,j) for i in range(h) for j in range(w) if g[i][j]!=bg]
    if not c:return g
    if any(i==0 for i,j in c):dy,dx=1,0
    elif any(i==h-1 for i,j in c):dy,dx=-1,0
    elif any(j==0 for i,j in c):dy,dx=0,1
    else:dy,dx=0,-1
    r=[[bg]*w for _ in range(h)];v=set()
    for i,j in c:
        if (i,j)in v:continue
        col=g[i][j];q=[(i,j)];v.add((i,j));A=[];ys=[];xs=[]
        while q:
            y,x=q.pop();A.append((y,x));ys.append(y);xs.append(x)
            for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                u,vv=y+a,x+b
                if 0<=u<h and 0<=vv<w and g[u][vv]==col and (u,vv)not in v:
                    v.add((u,vv));q.append((u,vv))
        sh=(max(ys)-min(ys)+1)*dy;sw=(max(xs)-min(xs)+1)*dx
        for y,x in A:
            ny, nx=y+sh,x+sw
            if 0<=ny<h and 0<=nx<w:r[ny][nx]=col
    return r
