# fill rectangle enclosed by 8s with 2
# Far from the best. hmm.
def p(g):
    mask=[0]*len(g[0])
    for r in g:
        mask=[c|m for c,m in zip(r,mask)]
    g=[[[c,2][8 in r and c<1 and m>0]for c,m in zip(r,mask)]for r in g]
    return g
