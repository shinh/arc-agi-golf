def p(g):
    h=len(g);w=len(g[0]);l=[r[:w//2]for r in g];r=[r[w//2+w%2:]for r in g]
    return l if l==r else g[:h//2]
