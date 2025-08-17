def p(g):
    o=[]
    #show(g,"in")
    for y in range(20):
        for x in range(20):
            if g[y][x]:
                ey,ex=y,x
                while ey<20 and g[ey][x]:ey+=1
                while ex<20 and g[y][ex]:ex+=1
                b=[[g[fy][fx]for fx in range(x,ex)]for fy in range(y,ey)]
                o+=(sum([c>1 for c in sum(b,[])]),len(b),len(b[0]),b),
    #show(max(o)[3],"out")
    return max(o)[3]
