def p(g):
    # draw lines of rare edge color
    a,*_,b=zip(*g);c=min({*a}&{*b}|{*g[0]}&{*g[-1]},key=sum(g,[]).count);return[[c*(r[0]==r[-1]==c or t==b==c)for t,b in zip(g[0],g[-1])]for r in g]
