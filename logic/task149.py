def p(g):
    o=create(3,3)
    for by in range(3):
        for bx in range(3):
            c=0
            for y in range(by*4,by*4+3):
                for x in range(bx*4,bx*4+3):
                    if g[y][x]==6:c+=1
            o[by][bx]=1 if c==2 else 0
    return o
