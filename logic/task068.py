def p(g):
    h=w=10;a=sum(g,[])
    v=[c for c in a if c and a.count(c)==1][0];y,x=divmod(a.index(v),w);o=create(h,w)
    for Y in-1,0,1:
        for X in-1,0,1:
            if 0<=y+Y<h and 0<=x+X<w:o[y+Y][x+X]=2
    o[y][x]=v;return o
