def p(g):
    h=len(g);w=len(g[0]);q=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]<2:g[y][x]=1
            if not y or not x or y==h-1 or x==w-1:q+=[(y,x)]
    while q:
        y,x=q.pop()
        if g[y][x]!=1:continue
        g[y][x]=0
        if y:q.append((y-1,x))
        if x:q.append((y,x-1))
        if y+1<h:q.append((y+1,x))
        if x+1<w:q.append((y,x+1))
    return g
