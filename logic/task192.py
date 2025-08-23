def p(g):
    # keep cells touching b both axes
    f=sum(g,[]);b=max({*f}-{0},key=f.count)
    return[[b*(b in sum(g[y:y+2]+g[y-1:y],[])[x::len(r)])*(b in r[x-1:x]+r[x+1:x+2]) if v*(v-b) else v for x,v in enumerate(r)]for y,r in enumerate(g)]
