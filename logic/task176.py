def p(g):
    h=len(g);w=len(g[0]);v=[[0]*w for _ in g];os=[]
    for i in range(h):
        for j in range(w):
            if g[i][j] or v[i][j]:continue
            q=[(i,j)];v[i][j]=1;o=[]
            while q:
                y,x=q.pop();o+=[(y,x)]
                for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                    u,vv=y+a,x+b
                    if 0<=u<h and 0<=vv<w and g[u][vv]==0 and not v[u][vv]:v[u][vv]=1;q+=[(u,vv)]
            os+=[o]
    os.sort(key=lambda o:sum(x for y,x in o)//len(o))
    for k,o in enumerate(os):
        if k%3==0:
            for y,x in o:g[y][x]=4
    return g
