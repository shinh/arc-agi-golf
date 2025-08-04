def p(g):
    h=len(g);w=len(g[0])
    bg=max(sum(g,[]),key=sum(g,[]).count)
    vis=[[0]*w for _ in range(h)];comp={}
    for y in range(h):
        for x in range(w):
            c=g[y][x]
            if c==bg or vis[y][x]:continue
            q=[(y,x)];vis[y][x]=1;cells=[]
            while q:
                i,j=q.pop();cells.append((i,j))
                for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                    u,v=i+a,j+b
                    if 0<=u<h and 0<=v<w and not vis[u][v] and g[u][v]==c:
                        vis[u][v]=1;q.append((u,v))
            comp.setdefault(c,[]).append(cells)
    colA=next(c for c,v in comp.items() if len(v)==2 and all(len(o)>1 and all(i in(0,h-1) or j in(0,w-1) for i,j in o) for o in v))
    colB=next(c for c in comp if c!=colA)
    A=comp[colA];B=[p for o in comp[colB] for p in o]
    rowsB={i for i,j in B};colsB={j for i,j in B}
    o1,o2=A if any(i in rowsB or j in colsB for i,j in A[0]) else A[::-1]
    res=[row[:] for row in g]
    cols1={x for y,x in o1};rows1={y for y,x in o1}
    for y,x in B:
        if x in cols1:
            t=min(rows1,key=lambda r:abs(r-y));s=1 if y<t else -1
            for yy in range(y+s,t,s):res[yy][x]=colB
        else:
            t=min(cols1,key=lambda c:abs(c-x));s=1 if x<t else -1
            for xx in range(x+s,t,s):res[y][xx]=colB
        res[y][x]=4
    rowsA={y for o in A for y,x in o};colsA={x for o in A for y,x in o}
    vert=len(rowsA)>len(colsA)
    def ul(o):
        ys=[y for y,x in o];xs=[x for y,x in o];return min(ys),min(xs)
    dy=ul(o2)[0]-ul(o1)[0];dx=ul(o2)[1]-ul(o1)[1]
    sh=(dy,0) if vert else (0,dx)
    for y,x in B:
        ny, nx=y+sh[0],x+sh[1]
        if 0<=ny<h and 0<=nx<w:
            if vert:
                for j in range(w):res[ny][j]=colB
            else:
                for i in range(h):res[i][nx]=colB
    for o in A:
        for y,x in o:res[y][x]=colA
    return res
