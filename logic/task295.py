def p(g):# grow block
 r=g[0];l=r.index(0);o=[r]
 for i in range(len(r)//2-1):r=r[:];r[l+i]=r[0];o+=r,
 return o
