def p(a):
 t,*_,b=[i for i,r in enumerate(a)if any(r)]
 c=max(i for i,r in enumerate(zip(*a))if any(r))
 v=a[t+1:b];M=sum(any(r[3:c])for r in v)-1
 for i in range(t,b+1):
  for j in range(2,c+1):
   if i in(t,b)or j in(2,c)or any(a[i][3:c])>M*M or any(r[j]for r in v)*M:a[i][j]=a[i][j]or 2
 return a
