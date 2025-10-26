def p(g):
 a,b=len(g),len(g[0])
 def f(i,j):
  if 0<=i<a and 0<=j<b and g[i][j]:
   g[i][j]=0;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1);return 1
  return 0
 r=range(sum(f(i,j)for i in range(a)for j in range(b)))
 return[[8*(i==j)for j in r]for i in r]
