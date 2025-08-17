def p(g):
    #show(g, "input")
    for t in range(4):
        if 5 in g[0]:
            for r in g:
                sx=r.index(5)
                s=len([c for c in r[:sx]if c])
                r[:sx]=[0]*(sx-s)+[5]*s
            #show(ng, "crop")

        g=[*map(list,zip(*g[::-1]))]
    return g