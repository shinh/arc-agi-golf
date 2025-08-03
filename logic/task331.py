def p(g):
    o=create(10,10)
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==1:
                o[y][x]=1
                if y:o[y-1][x]=2
                if x:o[y][x-1]=7
                if x<9:o[y][x+1]=6
                if y<9:o[y+1][x]=8
    return o
