def p(g):
    n=len(g);m=len(g[0]);o=[r[:] for r in g]
    for i in range(n-1):o[i][m-1-i]=2
    for j in range(1,m):o[-1][j]=4
    return o
