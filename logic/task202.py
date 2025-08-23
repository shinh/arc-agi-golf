# zero colored lines around holes
def p(g):
    for _ in[0]*4:t=next((r for r in g if 0<min(r)<max(r)),());g=tuple(zip(*[[v*all(b|v-a for a,b in zip(t,r))for v in r]for r in g][::-1]))
    return g
