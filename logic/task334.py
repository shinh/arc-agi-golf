def p(g):
    for r in g:
        for c in r:
            if c:
                if c==1:return[[0,5,0],[5,5,5],[0,5,0]]
                if c==2:return[[5,5,5],[0,5,0],[0,5,0]]
                return[[0,0,5],[0,0,5],[5,5,5]]
