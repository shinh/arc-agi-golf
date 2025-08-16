def p(g,l=len):# repeat blocks then map colors via first row
 n=l(g);g=[(x[:l({*g[0]})-1]*n)[:n]for x in g];g=(g[:l({x[0]for x in g})-1]*n)[:n];return[[g[0][g[0].index(y)+1]for y in r]for r in g]

