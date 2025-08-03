def p(g):
    k=0
    for r in g:
        if any(r):k+=1
        else:break
    g[-k:]=g[:k][::-1]
    return g
