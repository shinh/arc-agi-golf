def p(g):
 o=[r[:]for r in g]
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:
    for i in range(x+1,len(r)):o[y][i]=5 if(i-x)%2 else v
    break
 return o
