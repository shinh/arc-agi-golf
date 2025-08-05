def p(g):
    w=h=10
    for y in range(h):
        for x in range(w):
            if g[y][x] and g[y][x]!=5:break
        else:continue
        break
    v={(y,x)};s=[(y,x)];Y=[y];X=[x]
    while s:
        y,x=s.pop()
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and g[ny][nx] not in (0,5) and (ny,nx)not in v:
                v.add((ny,nx));s.append((ny,nx));Y.append(ny);X.append(nx)
    y0,y1=min(Y),max(Y);x0,x1=min(X),max(X)
    p=[r[x0:x1+1] for r in g[y0:y1+1]];ph=y1-y0+1;pw=x1-x0+1
    for y in range(h-ph+1):
        for x in range(w-pw+1):
            if all(g[y+dy][x+dx]==5 for dy in range(ph) for dx in range(pw)):
                for dy in range(ph):g[y+dy][x:x+pw]=p[dy][:]
    return g
