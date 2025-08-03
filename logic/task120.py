def p(g):
    h=len(g);w=len(g[0]);v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x] and (y,x) not in v:
                c=g[y][x];s=[(y,x)];v.add((y,x));ys=[y];xs=[x];r=[]
                while s:
                    y1,x1=s.pop();r.append((y1,x1))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==c and (ny,nx) not in v:
                            v.add((ny,nx));s.append((ny,nx));ys.append(ny);xs.append(nx)
                a,b=min(ys),max(ys);c1,d=min(xs),max(xs)
                if b-a>1 and d-c1>1:
                    for y1,x1 in r:
                        if a<y1<b and c1<x1<d:g[y1][x1]=8
    return g
