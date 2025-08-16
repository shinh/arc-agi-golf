def p(g):
 # We remove only a single pixel every 4 iterations.
 for _ in[0]*44:
  for y,r in enumerate(g):
   w=len(r);R=g[y-1]
   for x in range(w-1):
    if r[x-1]+r[x+1]<1and(r[x]-R[x])*r[x]*R[x]:del g[y];g+=[[0]*w]
  g=[*map(list,zip(*g[::-1]))]
 return g
