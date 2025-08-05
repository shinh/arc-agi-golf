def p(g):
    h=w=10;v=set();o=[]
    for y in range(h):
        for x in range(w):
            if (y,x)not in v:
                t=g[y][x];q=[(y,x)];v.add((y,x));s={(y,x)};a=b=y;c=d=x
                while q:
                    i,j=q.pop();a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=i+dy,j+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==t and (ny,nx)not in v:
                            v.add((ny,nx));q.append((ny,nx));s.add((ny,nx))
                if len(s)==(b-a+1)*(d-c+1):o.append((len(s),a,b,c,d))
    if o:
        mn=min(o)[1:];mx=max(o)[1:]
        for (a,b,c,d),k in((mn,1),(mx,2)):
            for y in range(a+1,b):
                for x in range(c+1,d):g[y][x]=k
    return g
