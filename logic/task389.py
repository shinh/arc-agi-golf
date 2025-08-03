def p(g):
    c=({*sum(g,[])}-{5}).pop()
    return [[c*(x==5) for x in r] for r in g]
