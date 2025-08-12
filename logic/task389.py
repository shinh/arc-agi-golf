# 66. Still 9B behind?
def p(g):
    return[[({*sum(g,[])}-{5}).pop()*(x==5)for x in r] for r in g]
