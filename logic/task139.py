def p(g):
    h=w=9;v=set();m=[]
    for y in range(h):
        for x in range(w):
            if g[y][x] and (y,x)not in v:
                t=g[y][x];q=[(y,x)];v.add((y,x));s={(y,x)};a=b=y;c=d=x
                while q:
                    i,j=q.pop();a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
                    for dy in(-1,0,1):
                        for dx in(-1,0,1):
                            if dy or dx:
                                ny,nx=i+dy,j+dx
                                if 0<=ny<h and 0<=nx<w and g[ny][nx]==t and (ny,nx)not in v:
                                    v.add((ny,nx));q.append((ny,nx));s.add((ny,nx))
                for i in range(a,b+1):
                    for j in range(c,d+1):
                        if (i,j)not in s:m.append((i,j))
    for i,j in m:g[i][j]=7
    return g
