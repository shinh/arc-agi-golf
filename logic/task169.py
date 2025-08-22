def p(g):
    # recolor 5-blocks by size
    for y in range(10):
        for x in range(10):
            if g[y][x]==5:
                q=[(y,x)];g[y][x]=0
                for i,j in q:
                    for A,B in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if 0<=A<10 and 0<=B<10 and g[A][B]==5:
                            g[A][B]=0;q+=(A,B),
                for i,j in q:g[i][j]=5-len(q)
    return g
