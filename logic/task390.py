# rotate to reuse horizontal logic.
# mirror values between the 2s outward.
def p(g):
 for _ in"r"*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if 2in r:c=r.index;s=c(2);k=s+2;m=c(2,s+1)-s-3>>1;r[s+~m:~-s],r[k:k+m]=r[k:k+m][::-1],[0]*m
 return g
