def p(g):
    from collections import Counter as C
    d=C(sum(g,[]));b=max(d,key=d.get)
    for c in d:
        if c-b:
            y,x=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c])
            if len(y)!=(max(y)-min(y)+1)*(max(x)-min(x)+1):return [[c]]
