def p(g):
    # fill diagonals with last seen color
    c=[0]*3
    for i,v in enumerate(sum(g,[])):
        if v:c[(i%7+i//7)%3]=v
    r=range(7)
    return[[c[(y+x)%3]for x in r]for y in r]
