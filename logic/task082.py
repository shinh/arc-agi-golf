# copy colors to horizontal neighbors then repeat rows
def p(g):
    a=[0,*g[0],0];l=len(g)
    return([g[0],[b or a for a,b in zip(a,a[2:])]]*l)[:l]
