# Not golfed yet.
# Note this is almost identical to task390.
def p(g):
 for _ in"r"*4:
  g=[*map(list,zip(*g[::-1]))]
  for r in g:
   if 2in r:c=r.index;s=c(2);m=c(2,s+1)-s-3>>1;r[s-m-1:s-1],r[s+2:s+m+2]=r[s+2:s+m+2][::-1],[0]*m
 return g
