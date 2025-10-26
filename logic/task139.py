def p(g):# fill 3x3 windows with 7
 for k in range(49):
  a=g[k//7:][:3];j=k%7;w=[r[j:j+3]for r in a]
  if min(map(sum,w+[*zip(*w)])):
   for r in a:r[j:j+3]=[x or 7for x in r[j:j+3]]
 return g
