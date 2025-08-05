def p(g):
    w=h=10
    o=create(h,w);v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x]==5 and (y,x)not in v:
                s=[(y,x)];a=[]
                while s:
                    y1,x1=s.pop()
                    if (y1,x1) in v or g[y1][x1]!=5:continue
                    v.add((y1,x1));a.append((y1,x1))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w:s.append((ny,nx))
                ys=[y for y,_ in a];xs=[x for _,x in a]
                t,b=min(ys),max(ys);l,r=min(xs),max(xs)
                for yy in range(t,b+1):
                    for xx in range(l,r+1):
                        o[yy][xx]=1 if yy in(t,b) and xx in(l,r) else 4 if yy in(t,b) or xx in(l,r) else 2
    return o
