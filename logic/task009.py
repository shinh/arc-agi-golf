def p(g,n=0):
    # connect same-colored dots
    for t in 0,1:
        g=[[[n:=[n,[0,-v][v in r[x+1:]]][v and v!=g[0][2]],v][v!=0]for x,v in enumerate(r)]for r in zip(*g)]
    g=[[abs(c)for c in r]for r in g]
    return g
