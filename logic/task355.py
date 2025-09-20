def p(g):# rare color's neighborhood majority color
    # majority colors around each rare cell, then majority of those
    M=lambda q:max(q,key=q.count);E=enumerate;p=min(f:=sum(g,[]),key=f.count);return[[M([M([w for Y,R in E(g)for X,w in E(R)if-5<Y-y<5 and-5<X-x<5 and w^p])for y,R in E(g)for x,v in E(R)if v==p])]]
