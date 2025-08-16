def p(j):# recursive flood fill
 A=len(j);c=len(j[0])
 def f(a,b):
  if 0<=a<A and 0<=b<c and j[a][b]==5:
   j[a][b]=0
   return[(a,b)]+f(a+1,b)+f(a-1,b)+f(a,b+1)+f(a,b-1)
  return[]
 E=[f(k,W)for k in range(A)for W in range(c)if j[k][W]==5]
 for J,w in zip(sorted(E,key=len),(2,4,1)):
  for a,C in J:j[a][C]=w
 return j
