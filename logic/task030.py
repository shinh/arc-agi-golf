def p(g):
 t={}
 for y,r in enumerate(g):
  for c in r:t.setdefault(c,y)
 u=t[1];o=[[0]*len(g[0])for _ in g]
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c:o[y+u-t[c]][x]=c
 return o
