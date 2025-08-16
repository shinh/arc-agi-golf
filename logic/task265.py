def p(g):
    # fill rectangles of zeros with 2
    o=[r[:]for r in g]
    for y in range(17):
        for x in range(17):
            if sum(g[y][x:x+2]+g[y+1][x:x+2])<1 and (y<1 or sum(g[y-1][x:x+2])) and (x<1 or g[y][x-1]+g[y+1][x-1]):
                X=x+2;Y=y+2
                while X<18 and g[y][X]+g[y+1][X]<1:X+=1
                while Y<18 and sum(g[Y][x:X])<1:Y+=1
                for r in o[y:Y]:r[x:X]=[2]*(X-x)
    return o

