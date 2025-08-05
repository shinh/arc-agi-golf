def p(g):
    h=w=10;j=next(i for i,v in enumerate(g[-1])if v);c=g[-1][j]
    o=[[0]*w for _ in g]
    for x in range(j,w,2):
        for y in range(h):o[y][x]=c
    for x in range(j+1,w,4):o[0][x]=5
    for x in range(j+3,w,4):o[-1][x]=5
    return o
