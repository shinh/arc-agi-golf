def p(g):
    h=len(g);w=len(g[0])
    for y in range(h):
        for x in range(w):
            if g[y][x]==5 and (y<1 or g[y-1][x]!=5) and (x<1 or g[y][x-1]!=5):
                X=x
                while X<w and g[y][X]==5:X+=1
                Y=y
                while Y<h and g[Y][x]==5:Y+=1
                for yy in range(y+1,Y-1):
                    for xx in range(x+1,X-1):g[yy][xx]=2
    return g
