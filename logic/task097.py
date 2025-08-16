def p(g):# zero isolated tiles
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c and sum(R[x-(x>0):x+2].count(c)for R in g[y-(y>0):y+2])<2:r[x]=0
 return g
