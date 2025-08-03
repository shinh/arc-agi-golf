def p(g):
    return [[1]] if g==g[::-1] and all(r==r[::-1] for r in g) else [[7]]
