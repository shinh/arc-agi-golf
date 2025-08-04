def p(g):
    n=len({c for r in g for c in r})
    return [[5]*3,[0]*3,[0]*3] if n<2 else([[5,0,0],[0,5,0],[0,0,5]]if n<3 else[[0,0,5],[0,5,0],[5,0,0]])
