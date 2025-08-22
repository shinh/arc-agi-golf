def p(g):# rare color's neighborhood majority color
    # majority colors around each rare cell, then majority of those
    p=min(f:=sum(g,[]),key=f.count);return[[max(u:=[max(m:=[v for R in g[max(0,y-4):y+5]for v in R[max(0,x-4):x+5]if v^p],key=m.count)for y,R in enumerate(g)for x,v in enumerate(R)if v==p],key=u.count)]]
