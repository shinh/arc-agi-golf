def p(g):
    # paint densest 3x3 block with its color
    r=range(3);s=range(0,9,4);m=0
    for y in s:
        for x in s:
            t=[g[y+i][x+j]for i in r for j in r if g[y+i][x+j]%5]
            m=max(m,len(t))
    for y in s:
        for x in s:
            t=[g[y+i][x+j]for i in r for j in r if g[y+i][x+j]%5]
            k=m and len(t)==m and t[0]
            for i in r:g[y+i][x:x+3]=[k]*3
    return g
