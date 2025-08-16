def p(g,e=enumerate):
    # pick colors from edges and paint 3s by row/col index
    t=g[0];u=g[-1];n=1>all(t+u);return[[(v,(t[0],(u[0],t[-1])[n])[(y,x)[n]>4])[v==3]for x,v in e(r)]for y,r in e(g)]
