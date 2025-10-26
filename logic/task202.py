# zero hole lines
def p(g):
    for _ in[0]*4:g=(*zip(*([v*all(b|v^a for a,b in zip(next((r for r in g if 0<min(r)<max(r)),()),r))for v in r]for r in g[::-1])),)
    return g
