def p(g):
    # crop inside markers
    for k in range(1,10):
        y,x=[[i for i,r in enumerate(t)if k in r]for t in(g,zip(*g))]
        if len(y)==2:
            return[[k*(v>0)for v in r[x[0]+1:x[1]]]for r in g[y[0]+1:y[1]]]

