def p(g):
    o=create(9,9)
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==5:
                for Y in range(y-1,y+2):
                    for X in range(x-1,x+2):
                        if 0<=Y<9 and 0<=X<9:o[Y][X]=1
    return o
