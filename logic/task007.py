def p(g):
    # fill diagonals with last seen color
    c=[0]*3
    for i,v in enumerate(sum(g,[])):
        if v:c[i%3]=v
    return[(c*3)[i%3:][:7]for i in range(7)]
