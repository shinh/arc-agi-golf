def p(g):
    # draw cross for each 2x2 block of 2s
    k=sum(sum(t)==8for r,s in zip(g,g[1:])for t in zip(r,r[1:],s,s[1:]))
    return[[k>int(c)for c in r]for r in('051','525','354')]
