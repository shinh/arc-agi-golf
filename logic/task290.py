# 127
# I don't know how to efficiently crop non-zero a region
def p(g):
    f=sum(g,[])
    f.sort(key=f.count)
    a=[*set(f)][1:]
    return[r for r in[[[a[c==a[0]],0][c<1]for c in r if c]for r in g]if r]
