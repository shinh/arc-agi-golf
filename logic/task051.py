def p(g):
    h=len(g);w=len(g[0]);f=sum(g,[])
    for c in range(1,10):
        if f.count(c)==1:break
    y,x=divmod(f.index(c),w)
    for dy,dx in((0,1),(1,0),(0,-1),(-1,0)):
        y1,x1=y+dy,x+dx;y2,x2=y-dy,x-dx
        if 0<=y1<h and 0<=x1<w and g[y1][x1] and not(0<=y2<h and 0<=x2<w and g[y2][x2]):
            while 0<=y1<h and 0<=x1<w and g[y1][x1]:y1+=dy;x1+=dx
            while 0<=y1<h and 0<=x1<w:g[y1][x1]=c;y1+=dy;x1+=dx
            break
    return g
