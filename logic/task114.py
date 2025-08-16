def p(g):#dup edge
    return[[0]+g[0]+[0],*[v[:1]+v+v[-1:]for v in g],[0]+g[-1]+[0]]
