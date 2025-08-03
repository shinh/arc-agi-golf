def p(g):
 t={}
 for y,r in enumerate(g):
  for c in r:t.setdefault(c,y)
 u=t[1];o=create(len(g),len(g[0]))
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c:o[y+u-t[c]][x]=c
 return o
