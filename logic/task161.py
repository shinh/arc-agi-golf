def p(g):return[[max({*x,r[0],r[-1]}-{*sum((R[1:-1]for R in g[1:-1]),[])}|{0})for x in zip(g[0],g[-1])]for r in g]
