def p(g):
 # flood-fill 5s from top row colors
 def f(i,j,c):
  if 0<=i<10>j>=0 and g[i][j]==5:g[i][j]=c;f(i+1,j,c);f(i-1,j,c);f(i,j+1,c);f(i,j-1,c)
 [[f(i,j,g[0][j])for i in range(1,10)]for j in range(10)if g[0][j]]
 return g

