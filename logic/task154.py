# Not golfed yet.
# Note this is almost identical to task390.
# copy left chunk to right then wipe it, rotating to cover all dirs
def p(g):
 for _ in[0]*4:
  g=[*map(list,zip(*g))][::-1]
  for r in g:
   if{2,5}<=set(r):s=r.index(2);r[s+2:s+4]=r[s-2],r[s-3];r[s-3:s-1]=0,0
 return g
