def p(g):
 # set 4s
 for r,k in zip(g,(224,65,2051)):
  for i in range(len(r)):
   if k&1<<i%12:r[i]=4
 return g
