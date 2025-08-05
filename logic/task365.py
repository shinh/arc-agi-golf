def p(g):
    h=len(g);w=len(g[0]);v=set();b=-1
    for y in range(h):
        for x in range(w):
            if g[y][x] and (y,x)not in v:
                s=[(y,x)];v.add((y,x));Y=[y];X=[x];c=a=0
                while s:
                    y1,x1=s.pop();a+=1;c+=g[y1][x1]==2
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx] and (ny,nx)not in v:
                            v.add((ny,nx));s.append((ny,nx));Y.append(ny);X.append(nx)
                y0,y1=min(Y),max(Y);x0,x1=min(X),max(X)
                if (y1-y0+1)*(x1-x0+1)==a and c>b:b=c;r=y0,y1,x0,x1
    y0,y1,x0,x1=r
    return [row[x0:x1+1] for row in g[y0:y1+1]]