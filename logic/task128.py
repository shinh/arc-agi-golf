# rot90 -> shift -> rot270
# 112 vs 72
def p(g):
    g=[[0]*(c:=r.index(0))+r[:15-c]for r in[[*r]for r in zip(*g[::-1])]]
    return[[*r]for r in zip(*g)][::-1]
