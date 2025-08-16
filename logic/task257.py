def p(g):
    # choose first nonzero among four corner samples
    return[[a[x]or a[x+5]or b[x]or b[x+5]for x in range(4)]for a,b in zip(g,g[5:])]
