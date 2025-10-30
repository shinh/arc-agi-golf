# rotate to reuse horizontal logic.
# mirror values between the 2s outward.
def p(g):
 for _ in"r"*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if 2in r:m=(c:=r.index)(2,(k:=c(2)+2)-1)+~k>>1;r[k-m-3:k-3],r[k:k+m]=r[k:k+m][::-1],[0]*m
 return g
