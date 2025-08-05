def p(g):
    for c in set(sum(g,[]))-{0}:
        y,x=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c])
        if len(y)!=(max(y)-min(y)+1)*(max(x)-min(x)+1):return [[c]]
