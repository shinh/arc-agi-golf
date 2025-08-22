def p(g):
    m=0,0,0,0
    #show(g,"in")
    for y in range(20):
        for x in range(20):
            if g[y][x]:
                ey=y
                while ey<20 and g[ey][x]:ey+=1
                ex=x
                while ex<20 and g[y][ex]:ex+=1
                b=[r[x:ex]for r in g[y:ey]]
                m=max(m,(sum(c>1for r in b for c in r),ey-y,ex-x,b))
    #show(m[3],"out")
    return m[3]
