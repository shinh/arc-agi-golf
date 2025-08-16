def p(g):
    # draw lines of rare edge color
    T,B=g[0],g[-1]
    c=min(({r[0]for r in g}&{r[-1]for r in g}|{*T}&{*B})-{0},key=sum(g,[]).count)
    return [[c*(r[0]==r[-1]==c or t==b==c)for t,b in zip(T,B)]for r in g]
