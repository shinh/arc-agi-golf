def p(g,l=len):# repeat blocks then map colors via first row
 a=l({r[0]for r in g})-1;r=g[0];s=range(l(g));return[[r[r.index(g[i%a][j%(l({*r})-1)])+1]for j in s]for i in s]
