# rot90 -> shift -> rot270
# 108 vs 72
def p(g):
    # How can we remove two r.index(0)?
    return[[*r]for r in zip(*[[0]*(r.index(0))+r[:15-r.index(0)]for r in[[*r]for r in zip(*g[::-1])]])][::-1]
