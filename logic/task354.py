def p(g):# flood top colors
 def f(i,j):
  if 0<=i<10>j>=0>=g[i][j]^5:g[i][j]=c;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 [f(k//10+1,k%10)for k in range(90)if(c:=g[0][k%10])];return g

