# zero colored lines around holes
def p(g):
    for _ in[0]*4:
        if t:=next((r for r in g if 0<min(r)<max(r)),0):
            g=[[v*all(v-a for a,b in zip(t,r)if b<1)for v in r]for r in g]
        g=[*map(list,zip(*g[::-1]))]
    return g
