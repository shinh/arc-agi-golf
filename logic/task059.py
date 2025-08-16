def p(g):
    # paint densest 3x3 block with its color
    r=0,1,2;s=0,4,8;m=0
    for y in s:
        for x in s:
            t=[a for i in r for j in r if (a:=g[y+i][x+j])%5]
            m=max(m,len(t))
    for y in s:
        for x in s:
            t=[a for i in r for j in r if (a:=g[y+i][x+j])%5]
            k=(len(t)==m)*sum(t[:1])
            for i in r:g[y+i][x:x+3]=[k]*3
    return g
