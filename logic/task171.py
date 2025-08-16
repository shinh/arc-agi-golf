def p(g):# border
    h=len(g);w=len(g[0])
    return[[8*(x*y*(w+~x)*(h+~y)<1)for x in range(w)]for y in range(h)]
