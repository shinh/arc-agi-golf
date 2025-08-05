def p(g):
    h=w=13
    seen=[[0]*w for _ in range(h)];objs=[]
    dirs=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(h):
        for j in range(w):
            if seen[i][j] or not g[i][j]:continue
            q=[(i,j)];seen[i][j]=1;o=[]
            while q:
                y,x=q.pop();o.append((y,x,g[y][x]))
                for dy,dx in dirs:
                    ny=y+dy;nx=x+dx
                    if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and g[ny][nx]:
                        seen[ny][nx]=1;q.append((ny,nx))
            objs.append(o)
    def norm(o):
        mn=min(y for y,_,_ in o);ml=min(x for _,x,_ in o)
        return [(c,y-mn,x-ml)for y,x,c in o]
    def anc(p,c):
        t=[(y,x)for col,y,x in p if col==c]
        return(min(t) if t else(0,0))
    out=[r[:]for r in g]
    # color3 pattern
    ob3=[o for o in objs if any(c==3 for _,_,c in o)]
    if ob3:
        p3=norm(max(ob3,key=lambda o:len({c for _,_,c in o})))
        ay,ax=anc(p3,3)
        for i in range(h):
            for j in range(w):
                if g[i][j]==3:
                    for c,dy,dx in p3:
                        y=i+dy-ay;x=j+dx-ax
                        if 0<=y<h and 0<=x<w:out[y][x]=c
    # color2 mirrored pattern
    ob2=[o for o in objs if any(c==2 for _,_,c in o)]
    if ob2:
        o2=max(ob2,key=lambda o:len({c for _,_,c in o}))
        minc=min(x for y,x,_ in o2);maxc=max(x for y,x,_ in o2)
        p2=[(c,y,maxc-(x-minc))for y,x,c in o2]
        p2=norm([(y,x,c)for c,y,x in p2])
        ay,ax=anc(p2,2)
        orig={(y,x)for y,x,c in o2 if c==2}
        for i in range(h):
            for j in range(w):
                if g[i][j]==2 and (i,j) not in orig:
                    for c,dy,dx in p2:
                        y=i+dy-ay;x=j+dx-ax
                        if 0<=y<h and 0<=x<w:out[y][x]=c
    return out
