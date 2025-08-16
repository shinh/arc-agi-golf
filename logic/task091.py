def p(g):
    y,x=zip(*((j,i)for j,r in enumerate(g)for i,v in enumerate(r)if v==5))
    return[r[min(x):max(x)+1]for r in g[max(0,min(y)-1):max(y)+2]]
