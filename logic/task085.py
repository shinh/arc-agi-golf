# 147
def p(g):
    for r,nr,pr in zip(g,g[-1:]+g,g[1:]+g):
        for x in range(len(r)):
            if len(set([r[x],nr[x],pr[x],r[x-1],(r+[0])[x+1]]))==1:
                r[x]=0
    return g
