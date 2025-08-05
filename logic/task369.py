def p(g):
    w=h=10;v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and (y,x)not in v:
                s=[(y,x)];v.add((y,x));c=[]
                while s:
                    y1,x1=s.pop();c.append((y1,x1))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==0 and (ny,nx)not in v:
                            v.add((ny,nx));s.append((ny,nx))
                k=3 if len(c)==1 else 2 if len(c)==2 else 1
                for y1,x1 in c:g[y1][x1]=k
    return g
