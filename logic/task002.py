def p(g):
    h=len(g);w=len(g[0])
    v={}
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and (y,x) not in v:
                s=[(y,x)];r=[];e=1
                while s:
                    y1,x1=s.pop()
                    if (y1,x1) in v or g[y1][x1]: continue
                    v[(y1,x1)]=1;r.append((y1,x1))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y1+dy,x1+dx
                        if ny<0 or ny>=h or nx<0 or nx>=w:
                            e=0
                        else:
                            c=g[ny][nx]
                            if c==0:s+=[(ny,nx)]
                            elif c!=3:e=0
                if e:
                    for y1,x1 in r: g[y1][x1]=4
    return g
