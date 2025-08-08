def p(g):
    for c in range(1,10):
        if len(set(r.count(c)for r in g))>2:
            return[[c]]

