def p(g):
    # extend the lone colored cell toward its neighbor
    h=len(g);w=len(g[0]);f=sum(g,[])
    for c in f:
        if f.count(c)==1:break
    y,x=divmod(f.index(c),w)
    for dy,dx in((0,1),(1,0),(0,-1),(-1,0)):
        y1,x1=y+dy,x+dx
        if h>y1>=0<=x1<w and g[y1][x1] and not(h>y-dy>=0<=x-dx<w and g[y-dy][x-dx]):
            while h>y1>=0<=x1<w and g[y1][x1]:y1+=dy;x1+=dx
            while h>y1>=0<=x1<w:g[y1][x1]=c;y1+=dy;x1+=dx
            break
    return g
