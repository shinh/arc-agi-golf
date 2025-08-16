def p(g):#find top-left color and crop 3x3
    y,x=[[*map(any,f)].index(1)for f in(g,zip(*g))]
    return[r[x:x+3]for r in g[y:y+3]]
