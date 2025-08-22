# Not bad, but not golfed yet.
# 120
def p(o):
    for c in sum(o,[]):
        g=o
        for _ in g*8:g=[*zip(*g[(c in g[-1])-2::-1])]
        if[g[::-1]for g in g]==g:return g
