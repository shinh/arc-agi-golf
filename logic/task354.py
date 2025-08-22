def p(g):
 # flood-fill 5s from top row colors
 def f(i,j):
  if 0<=i<10>j>=0==g[i][j]-5:g[i][j]=c;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 [f(i+1,j)for j in range(10)if(c:=g[0][j])for i in range(9)]
 return g

