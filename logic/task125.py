def p(g):
    h=w=15;o=[r[:]for r in g];v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x]==6 and (y,x)not in v:
                s=[(y,x)];Y=[];X=[]
                while s:
                    y1,x1=s.pop()
                    if(y1,x1)in v:continue
                    v.add((y1,x1));Y+=[y1];X+=[x1]
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==6 and (ny,nx)not in v:s.append((ny,nx))
                r0=max(min(Y)-1,0);r1=min(max(Y)+2,h);c0=max(min(X)-1,0);c1=min(max(X)+2,w)
                for yy in range(r0,r1):
                    for xx in range(c0,c1):
                        if yy in (r0,r1-1) or xx in (c0,c1-1):o[yy][xx]=3
                        elif g[yy][xx]!=6:o[yy][xx]=4
    return o
