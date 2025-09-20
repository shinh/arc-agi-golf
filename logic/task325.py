def p(m,K=range):# flood
 r,c=len(m),len(m[0])
 def f(y,x):
  if m[y][x]:m[y][x]=0;y+1<r and f(y+1,x);y and f(y-1,x);x+1<c and f(y,x+1);x and f(y,x-1);return 1
 n=sum(m[i][j]and f(i,j)for i in K(r)for j in K(c));return[[8*(i==j)for j in K(n)]for i in K(n)]
