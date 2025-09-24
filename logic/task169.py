def p(g):
    # recolor 5-blocks by size
    def f(y,x):
        if 9>=y>=0<=x<=9 and g[y][x]==5:
            g[y][x]=0;q.append((y,x))
            f(y+1,x);f(y-1,x);f(y,x+1);f(y,x-1)
    for y in range(10):
        for x in range(10):
            if g[y][x]==5:
                q=[];f(y,x)
                for i,j in q:g[i][j]=5-len(q)
    return g
