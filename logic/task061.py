def p(g,R=range(18)):
    p=[{*r}<={0,1} for r in g].index(1,1)
    return [[max(max(r[x%p::p]) for r in g[y%p::p])for x in R]for y in R]

