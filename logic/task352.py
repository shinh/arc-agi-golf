def p(g):# expand 1s around 2s
 e=enumerate
 for y,r in e(g):
  for x,v in e(r):
   if v==2:
    c=x-(x>0)
    for R in g[y-(y>0):y+2]:R[c:x+2]=[q or 1 for q in R[c:x+2]]
 return g

