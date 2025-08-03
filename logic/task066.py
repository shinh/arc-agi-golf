def p(g):
    h=len(g);w=len(g[0])
    s=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==3]
    t=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2]
    (y1,x1),(y2,x2)=s;v=x1==x2
    (a1,b1),(a2,b2)=t
    C=[(min(a1,a2)-1,b1),(max(a1,a2)+1,b1)] if b1==b2 else [(a1,min(b1,b2)-1),(a1,max(b1,b2)+1)]
    d=lambda p:min(abs(p[0]-y)+abs(p[1]-x)for y,x in s)
    C=[c for c in C if 0<=c[0]<h and 0<=c[1]<w and g[c[0]][c[1]]==0];C.sort(key=d)
    cand=set()
    for y,x in t:
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and g[ny][nx]==0:cand.add((ny,nx))
    for c in sorted(cand,key=d):
        if c not in C:C.append(c)
    def m(y,x,dy,dx):
        while 0<=y<h and 0<=x<w and g[y][x]==0:g[y][x]=3;y+=dy;x+=dx
        return y-dy,x-dx
    for z in C:
        if v:
            d1=-1 if z[0]<y1 else 1
            for k in (d1,-d1):
                sy=(y1-1 if k<0 else y2+1);sx=x1
                if not(0<=sy<h and g[sy][sx]==0):continue
                y,x=m(sy,sx,k,0)
                dx=1 if z[1]>x else -1
                y,x=m(y,x+dx,0,dx)
                dy=1 if z[0]>y else -1
                y,x=m(y+dy,x,dy,0)
                if (y,x)==z:return g
        else:
            d1=-1 if z[1]<x1 else 1
            for k in (d1,-d1):
                sx=(x1-1 if k<0 else x2+1);sy=y1
                if not(0<=sx<w and g[sy][sx]==0):continue
                y,x=m(sy,sx,0,k)
                dy=1 if z[0]>y else -1
                y,x=m(y+dy,x,dy,0)
                dx=1 if z[1]>x else -1
                y,x=m(y,x+dx,0,dx)
                if (y,x)==z:return g
    return g
