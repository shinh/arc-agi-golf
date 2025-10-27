def p(a):
 i,d=len(a),len(a[0])
 def r(n,e):
  if 0<=n<i and 0<=e<d and a[n][e]:
   a[n][e]=0;r(n+1,e);r(n-1,e);r(n,e+1);r(n,e-1);return 1
  return 0
 o=range(sum(r(n,e)for e in range(d)for n in range(i)))
 return[[8*(n==e)for e in o]for n in o]
