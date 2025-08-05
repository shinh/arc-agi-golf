def p(g):
    w,h=5,3;o=create(h,w)
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:
                if y and x:o[y-1][x-1]=3
                if y and x+1<w:o[y-1][x+1]=6
                if y+1<h and x:o[y+1][x-1]=8
                if y+1<h and x+1<w:o[y+1][x+1]=7
    return o
