def p(g):
    s=g[0][0]==0
    for x in range(0,len(g[0]),3):
        r=(x//3+s)%2
        g[r][x]=g[r+1][x]=6
    return g
