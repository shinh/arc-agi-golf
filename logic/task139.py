def p(g):
 for k in range(49):
  i=k//7;j=k%7;a=g[i:i+3];w=[r[j:j+3]for r in a]
  if min(map(sum,w+[*zip(*w)])):
   for r in a:r[j:j+3]=[x or 7for x in r[j:j+3]]
 return g