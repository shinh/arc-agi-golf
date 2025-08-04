def p(g):
    h=len(g);w=len(g[0])
    bg=max(sum(g,[]),key=sum(g,[]).count)
    o=[r[:]for r in g]
    seen=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if seen[i][j] or g[i][j]==bg:continue
            q=[(i,j)];seen[i][j]=1;pts=[]
            while q:
                y,x=q.pop();pts.append((y,x,g[y][x]))
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and g[ny][nx]!=bg:
                        seen[ny][nx]=1;q.append((ny,nx))
            colors={c for _,_,c in pts};a=pts[0][2];b=(colors-{a}).pop()
            ys=[y for y,_,_ in pts];xs=[x for _,x,_ in pts]
            mn,mx=min(ys),max(ys);ln,rx=min(xs),max(xs)
            dh=(mx-mn+1)-2;dw=(rx-ln+1)-2
            for y in range(mn,mx+1):
                for x in range(ln,rx+1):o[y][x]=a
            for y,x,_ in pts:
                for ny in (y-dh,y+dh):
                    if 0<=ny<h:o[ny][x]=a
                for nx in (x-dw,x+dw):
                    if 0<=nx<w:o[y][nx]=a
            for x in range(ln,rx+1):
                o[mn][x]=b;o[mx][x]=b
            for y in range(mn,mx+1):
                o[y][ln]=b;o[y][rx]=b
    return o
