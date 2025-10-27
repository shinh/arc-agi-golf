def p(g):I={*sum((r[1:-1]for r in g[1:-1]),[])};return[[max({*x,r[0],r[-1]}-I|{0})for x in zip(g[0],g[-1])]for r in g]
