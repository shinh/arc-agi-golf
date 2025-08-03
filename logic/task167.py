def p(g):
    if len({c for r in g for c in r})==1:return [[5]*3,[0]*3,[0]*3]
    return [[5,0,0],[0,5,0],[0,0,5]] if g[0][0]<g[2][2] else [[0,0,5],[0,5,0],[5,0,0]]
