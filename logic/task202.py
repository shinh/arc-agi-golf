# zero hole lines
def p(g):
    for _ in[0]*4:t=next((r for r in g if max(r)>min(r)>0),());g=(*zip(*([v*all(b|v^a for a,b in zip(t,r))for v in r]for r in g[::-1])),)
    return g
