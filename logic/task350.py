def p(g):
 # link 1s in both axes
 for _ in 0,1:
  for r in g:
   q=[i for i,v in enumerate(r)if v==1]
   for a,b in zip(q,q[1:]):r[a+1:b]=[8]*(b-a-1)
  g=[*map(list,zip(*g))]
 return g

