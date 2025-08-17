def p(g):
    objs=[]
    for x in range(len(g[0])-2):
        for y in range(len(g)-2):
            o=[[g[oy][ox]for ox in range(x,x+3)]for oy in range(y,y+3)]
            s=set(sum(o,[]))
            if len(s)>1 and len(s&{0})<1:
                objs+=o,
                for oy in range(y,y+3):
                    for ox in range(x,x+3):
                        g[oy][ox]=0

    g=[*map(list,eval('zip(*filter(any,'*2+'g))))'))]
    #show(g, "crop")
    #print(len(objs))

    for o in objs:
        #print(o)
        yet=1
        for t in range(4):
            if yet:
                for y in range(len(g)-2):
                    for x in range(len(g[0])-2):
                        if all((o[oy][ox]!=2)==(g[y+oy][x+ox]>0)for oy in range(3)for ox in range(3))and yet:
                            for oy in range(3):
                                for ox in range(3):
                                    g[y+oy][x+ox]=o[oy][ox]
                            yet=0

            # Probably better to rotate o instead of g, though
            o=[*map(list,zip(*o[::-1]))]

    return g
