def p(g):
    h=len(g);w=len(g[0]);c={}
    for r in g:
        for v in r:c[v]=c.get(v,0)+1
    b=max(c,key=c.get)
    def o():
        v=[[0]*w for _ in g];R=[]
        for y in range(h):
            for x in range(w):
                if g[y][x]!=b and not v[y][x]:
                    d=g[y][x];s=[(y,x)];pts=[]
                    while s:
                        i,j=s.pop()
                        if v[i][j] or g[i][j]!=d:continue
                        v[i][j]=1;pts.append((i,j))
                        if i:s.append((i-1,j))
                        if j:s.append((i,j-1))
                        if i<h-1:s.append((i+1,j))
                        if j<w-1:s.append((i,j+1))
                    R.append((d,pts))
        return R
    for d,pts in o():
        if len(pts)<3:
            for y,x in pts:g[y][x]=b
    for d,pts in o():
        ys=[y for y,x in pts];xs=[x for y,x in pts]
        for y in range(min(ys),max(ys)+1):
            r=g[y]
            for x in range(min(xs),max(xs)+1):r[x]=d
    return g

