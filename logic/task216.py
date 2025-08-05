def p(g):
    w=h=20;v=set();m=-1
    for y in range(h):
        for x in range(w):
            if g[y][x] and (y,x)not in v:
                q=[(y,x)];v.add((y,x));Y=[y,y];X=[x,x];c=g[y][x]==2
                while q:
                    i,j=q.pop()
                    for u,vv in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if 0<=u<h and 0<=vv<w and g[u][vv] and (u,vv)not in v:
                            v.add((u,vv));q.append((u,vv))
                            Y[0]=min(Y[0],u);Y[1]=max(Y[1],u);X[0]=min(X[0],vv);X[1]=max(X[1],vv);c+=g[u][vv]==2
                if c>m:m=c;b=Y+X
    y1,y2,x1,x2=b
    return [r[x1:x2+1] for r in g[y1:y2+1]]
