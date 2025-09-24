def p(g):
    # keep cells touching b both axes
    f=sum(g,[]);b=max({*f}-{0},key=f.count);c=[*zip(*g)]
    return[[b*(b in c[x][y-(y>0):y+2])*(b in r[x-(x>0):x+2])if v*(v-b)else v for x,v in enumerate(r)]for y,r in enumerate(g)]
