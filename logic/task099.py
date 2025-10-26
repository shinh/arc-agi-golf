def p(g):
 for l in 0,1,4:
  k=[(r[l+2],i)for i,r in enumerate(g)if r[l]*r[l+4]]
  if k:
   for r in g[k[0][1]-1:k[-1][1]+1]:
    r[l:l+5]=[v or max(k)[0]for v in r[l:l+5]]
 return g
