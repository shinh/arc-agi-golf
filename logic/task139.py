def p(g):
 for k in range(49):
  a=g[k//7:][:3];w=[r[(j:=k%7):j+3]for r in a]
  if min(map(sum,w+[*zip(*w)])):
   for r in a:r[j:j+3]=[x or 7for x in r[j:j+3]]
 return g