# Not bad, but not golfed yet.
# 141
def p(o):
    for c in sum(o,[]):
        g=o
        for i in range(80):
            g=[*map(list,zip(*g[-2+(c in g[-1])::-1]))]
        if all(r==r[::-1]for r in g):
            return g
