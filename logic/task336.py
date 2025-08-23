def p(g):#fill gaps after 5s in any direction
    for _ in[0]*4:
        for r,nr in zip(g,g[1:]):
            if 0<(n:=r.count(5))<3:
                a=r.index(5);e=(9-r[::-1].index(5),10)[n<2>nr.index(5)^a==0];r[a+1:e]=[8]*~(a-e)
        g=[*map(list,zip(*g[::-1]))]
    return g
