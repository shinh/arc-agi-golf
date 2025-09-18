def p(g,k=1):
    # crop inside markers
    y,x=[[i for i,r in enumerate(t)if k in r]for t in(g,zip(*g))]
    return p(g,k+1)if len(y)!=2 else[[k*(v>0)for v in r[x[0]+1:x[1]]]for r in g[y[0]+1:y[1]]]

