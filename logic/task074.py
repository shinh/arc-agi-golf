r=range(30)
m=min
def p(a):
 for _ in 0,1:
  for i in r:
   for j in r:x,y=max((h:=m(i,31-i)),(k:=m(j,31-j))),m(h,k);a[x][y]=a[i][j]=m(a[i][j],a[x][y])
 return a