def p(g):
    h,w=len(g),len(g[0]);g=[r[:]for r in g]
    b=max({v for r in g for v in r},key=lambda v:sum(r.count(v)for r in g))
    s=set()
    for i in range(h):
        for j in range(w):
            if g[i][j]!=b and(i,j)not in s:
                c=g[i][j];q=[(i,j)];t={(i,j)};s.add((i,j));xs=[i];ys=[j]
                while q:
                    x,y=q.pop()
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and g[nx][ny]==c and(nx,ny)not in s:
                            s.add((nx,ny));q+=[(nx,ny)];t.add((nx,ny));xs+=[nx];ys+=[ny]
                mnx,mxx=min(xs),max(xs);mny,mxy=min(ys),max(ys)
                for (cx,cy),(dx,dy) in[((mxx,mxy),(1,1)),((mnx,mxy),(-1,1)),((mxx,mny),(1,-1)),((mnx,mny),(-1,-1))]:
                    if(cx,cy)not in t:
                        x,y=cx+dx,cy+dy
                        while 0<=x<h and 0<=y<w:g[x][y]=c;x+=dx;y+=dy
    return g
