def p(g):#stripe
 E,t=enumerate,0
 i,j,v=next((i,j,v)for i,a in E(g)for j,v in E(a)if v%5)
 while j<10:
  for a in g[:i+1]:a[j]=v
  if j-9:g[t*9][j+1]=5;t^=1
  j+=2
 return g

