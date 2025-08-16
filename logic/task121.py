def p(g):#3x3 around 8->center=2nd max
    y,x=divmod(sum(g,[]).index(8),len(g[0]));g=[t[x-1:x+2]for t in g[y-1:y+2]];g[1][1]=sorted(sum(g,[]))[7];return g
