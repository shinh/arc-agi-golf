def p(a):
 u=[i for i,r in enumerate(a)if any(r)];t,b=u[0],u[-1]
 c=max(i for i in range(13)if any(r[i]for r in a))
 L=sum(any(a[i][3:c])for i in range(t+1,b))
 for i in range(t,b+1):
  for j in range(2,c+1):
   if i in(t,b)or j in(2,c)or any(a[i][3:c])==L==1 or any(a[k][j]for k in range(t+1,b))and L-1:a[i][j]=a[i][j]or 2
 return a