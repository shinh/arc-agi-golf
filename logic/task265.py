def p(g):
    w=h=18;o=[r[:]for r in g]
    for y in range(h-1):
        for x in range(w-1):
            if g[y][x]==g[y][x+1]==g[y+1][x]==g[y+1][x+1]==0 and (y<1 or g[y-1][x] or g[y-1][x+1]) and (x<1 or g[y][x-1] or g[y+1][x-1]):
                X=x+2
                while X<w and g[y][X]==g[y+1][X]==0:X+=1
                Y=y+2
                while Y<h and all(g[Y][i]==0 for i in range(x,X)):Y+=1
                for yy in range(y,Y):o[yy][x:X]=[2]*(X-x)
    return o

