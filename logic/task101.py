def p(g):
    h=len(g);w=len(g[0]);D=(1,0,-1,0,1)
    for y,r in enumerate(g):
        if 1 in r:
            x=r.index(1);break
    s=[(y,x)];c={(y,x)}
    while s:
        y,x=s.pop()
        for d in range(4):
            a,b=y+D[d],x+D[d+1]
            if 0<=a<h and 0<=b<w and g[a][b] and(a,b)not in c:
                c.add((a,b));s.append((a,b))
    r0=min(y for y,_ in c);r1=max(y for y,_ in c)+1
    c0=min(x for _,x in c);c1=max(x for _,x in c)+1
    t=[row[c0:c1]for row in g[r0:r1]]
    P=[(i,j)for i,r in enumerate(t)for j,v in enumerate(r)if v==2]
    a=P[0];H=len(t);W=len(t[0])
    reg={(r0+i,c0+j)for i in range(H)for j in range(W)}
    out=[r[:]for r in g];seen=set();cl=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==2 and(y,x)not in reg and(y,x)not in seen:
                q=[(y,x)];seen.add((y,x));cells=[]
                while q:
                    Y,X=q.pop();cells.append((Y,X))
                    for d in range(4):
                        A,B=Y+D[d],X+D[d+1]
                        if 0<=A<h and 0<=B<w and g[A][B]==2 and(A,B)not in reg and(A,B)not in seen:
                            seen.add((A,B));q.append((A,B))
                my=min(y for y,_ in cells);mx=min(x for _,x in cells)
                k=max(y for y,_ in cells)-my+1
                cl.append((my,mx,k))
    used=set()
    for y,x,k in cl:
        if (y,x,k)in used:continue
        by=y-a[0]*k;bx=x-a[1]*k
        for py,px in P:used.add((by+py*k,bx+px*k,k))
        for i in range(H):
            for j in range(W):
                v=t[i][j]
                if v:
                    for di in range(k):
                        for dj in range(k):
                            Y=by+i*k+di;X=bx+j*k+dj
                            if 0<=Y<h and 0<=X<w:out[Y][X]=v
    return out
