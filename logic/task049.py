def p(g):
    s=sum(g,[]);c=s.count;k=min({*s}-{0},key=c);h=sum(k in r for r in g)
    return [[k]*(c(k)//h)]*h