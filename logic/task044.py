def p(g):
    h=w=10;D=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    z=[];v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and (y,x) not in v:
                s=[(y,x)];c=[];e=1
                while s:
                    y1,x1=s.pop()
                    if (y1,x1) in v or g[y1][x1]!=0:continue
                    v.add((y1,x1));c.append((y1,x1))
                    for dy,dx in D:
                        ny=y1+dy;nx=x1+dx
                        if 0<=ny<h and 0<=nx<w:
                            t=g[ny][nx]
                            if t==0:s.append((ny,nx))
                            elif t!=5:e=0
                        else:e=0
                if e:z.append(c)
    o={};v=set();cnt=[0]*10
    for y in range(h):
        for x in range(w):
            c=g[y][x]
            if c and c!=5 and (y,x) not in v:
                s=[(y,x)];r=[]
                while s:
                    y1,x1=s.pop()
                    if (y1,x1) in v or g[y1][x1]!=c:continue
                    v.add((y1,x1));r.append((y1,x1))
                    for dy,dx in D:
                        ny=y1+dy;nx=x1+dx
                        if 0<=ny<h and 0<=nx<w:s.append((ny,nx))
                cnt[c]+=1
                m=min(y for y,x in r);n=min(x for y,x in r)
                k=tuple(sorted((y-m,x-n) for y,x in r))
                o.setdefault(k,[]).append((r,c))
    for c in z:
        m=min(y for y,x in c);n=min(x for y,x in c)
        k=tuple(sorted((y-m,x-n) for y,x in c))
        if k in o:
            a=o[k]
            j=next((i for i,(r,col) in enumerate(a) if cnt[col]==1),-1)
            if j+1:
                r,col=a.pop(j)
                for y,x in r:g[y][x]=0
                for y,x in c:g[y][x]=col
    return g
