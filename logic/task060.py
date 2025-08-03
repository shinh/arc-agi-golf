def p(g):
    for r in g:
        if r[0]|r[-1]:
            r[:5]=[r[0]]*5;r[5]=5;r[6:]=[r[-1]]*5
    return g
