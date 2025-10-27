def p(g):#show(g,"input")
    for _ in' '*4:
        for r in(g:=[*map(list,zip(*g[::-1]))])*(5in g[0]):i=r.index(5);r[:i]=sorted((x>0)*5for x in r[:i])#show(ng,"crop")
    return g

