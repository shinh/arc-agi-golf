def p(g):
    a=g[0][0];h,w=[sum(a not in r for r in t)+1 for t in (g,zip(*g))];return[[a]*w]*h # fill top-left color block
