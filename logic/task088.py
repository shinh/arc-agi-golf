def p(g):
    # crop inside markers
    for k in range(1,10):
        y=[i for i,r in enumerate(g)if k in r]
        if len(y)==2:
            x=[i for i,r in enumerate(zip(*g))if k in r]
            return[[k*(v>0)for v in r[x[0]+1:x[1]]]for r in g[y[0]+1:y[1]]]

