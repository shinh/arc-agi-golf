def p(g):# We remove only a single pixel every 4 iterations.
 for _ in[0]*44:
  for y,r in enumerate(g):
   R=g[y-1];W=len(r)
   for x in range(W-1):
    if r[x-1]+r[x+1]<1>0<R[x]!=r[x]>0:g+=[0]*W,;del g[y]
  g=[*zip(*g[::-1])]
 return g
