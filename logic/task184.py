def p(g):f=lambda a:[-1]+[i for i,x in enumerate(a)if max(x)<1];return[[max(g[i+1][j+1:j+4]+g[i+3][j+1:j+4])for j in f(zip(*g))]for i in f(g)]
