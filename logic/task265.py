def p(g):
    # fill rectangles of zeros with 2
    o=[r[:]for r in g]
    R=range(17)
    for y in R:
        for x in R:
            if sum(g[y][x:x+2]+g[y+1][x:x+2])<1 and (y<1 or sum(g[y-1][x:x+2])) and (x<1 or g[y][x-1]+g[y+1][x-1]):
                X=x+2
                while X<18>g[y][X]+g[y+1][X]==0:X+=1
                Y=y;w=[2]*(X-x)
                while Y<18>sum(g[Y][x:X])==0:o[Y][x:X]=w;Y+=1
    return o

