def p(g):
    def hsplit():
        return [[r[i*3:(i+1)*3] for r in g] for i in range(3)]
    for pce in hsplit():
        if pce!=[list(r) for r in zip(*pce)]:return pce
