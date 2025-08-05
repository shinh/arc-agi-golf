def p(g):
    return[[[7]],[[1]]][g==g[::-1] and all(r==r[::-1] for r in g)]
