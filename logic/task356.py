def p(g):
 # link
 h=map(list,g)
 for _ in 0,1:
  for r,H in zip(h,g):
   t=[i for i,v in enumerate(r)if v]
   if t[1:]:b=t[-1];H[t[0]:b+1]=[8]*-~(b-t[0])
  h=zip(*h)
  g=[*map(list,zip(*g))]
 return g
