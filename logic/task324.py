# draw diagonals from isolated colors
def p(g):
    h=len(g);w=len(g[0]);d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):d.setdefault(v,[]).append((y,x))
    r=[(c,max({*L},key=L.count),s)for c,s in d.items()if c not in(L:=[g[Y][X]for y,x in s for Y in range(y-(y>0),y+(y<h-1)+1)for X in range(x-(x>0),x+(x<w-1)+1)if Y-y or X-x])]
    a,ca,pa=r[0];b,cb,pb=r[-1];P=pa+pb;A={y-x for y,x in P};B={y+x for y,x in P}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if(y-x in A or y+x in B)and v in(ca,cb):g[y][x]=(a,b)[v==cb]
    return g
