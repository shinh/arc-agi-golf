def p(g):
    h=len(g);w=len(g[0])
    b={};r={}
    for y,row in enumerate(g):
        for x,c in enumerate(row):
            if c:
                if c in b:
                    if y>b[c]:b[c]=y
                    if x>r[c]:r[c]=x
                else:b[c]=y;r[c]=x
    o=create(h,w)
    for y,row in enumerate(g):
        for x,c in enumerate(row):
            if c:
                if y<b[c] and x<r[c] and x+1<w:o[y][x+1]=c
                else:o[y][x]=c
    return o
