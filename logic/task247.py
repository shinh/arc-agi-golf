def p(g):# flatten and count
    s=sum(g,[])
    t=sorted((s.count(i),s.index(i)%len(g[0]),i)for i in {*s}-{0})
    m=t[-1][0];return[[i for a,b,i in t if a==m]]*m
