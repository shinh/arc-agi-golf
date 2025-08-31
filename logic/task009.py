def p(g,n=0):
    # connect same dots
    for t in 0,1:
        g=[[[n:=[n,-v*(v in r[x+1:])][0<v!=g[0][2]],v][v!=0]for x,v in enumerate(r)]for r in zip(*g)]
    return[list(map(abs,r))for r in g]
