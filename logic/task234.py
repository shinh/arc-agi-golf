def p(g):
 # We remove only a single pixel every 4 iterations.
 for _ in[0]*44:
  for y,r in enumerate(g):
   L=len(R:=g[y-1])
   for x in range(L-1):
    if(r[x-1]+r[x+1]<1)*(0<R[x]!=r[x]>0):g+=[0]*L,;del g[y]
  g=[*zip(*g[::-1])]
 return g
