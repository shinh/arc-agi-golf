def p(g):# keep cells near b
    f=sum(g,[]);b=max({*f}-{0},key=f.count);*c,=zip(*g);e=enumerate;return[[b*(v and b in c[x][y-(y>0):y+2]and b in r[x-(x>0):x+2]or v==b)for x,v in e(r)]for y,r in e(g)]
