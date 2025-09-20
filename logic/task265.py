def p(g):
    # fill rectangles of zeros with 2
    o=[r[:]for r in g]
    for y in range(17):
        for x in range(17):
            if sum(g[y][x:x+2]+g[y+1][x:x+2]) or y and sum(g[y-1][x:x+2])<1 or x and g[y][x-1]+g[y+1][x-1]<1:continue
            X=x+2;Y=y
            while X<18>g[y][X]+g[y+1][X]<1:X+=1
            while Y<18>sum(g[Y][x:X])<1:o[Y][x:X]=[2]*(X-x);Y+=1
    return o

