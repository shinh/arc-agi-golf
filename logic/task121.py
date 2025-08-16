def p(g):
    y,x=divmod(sum(g,[]).index(8),len(g[0]));g=[t[x-1:x+2]for t in g[y-1:y+2]];g[1][1]=sorted(sum(g,[]))[-2];return g
