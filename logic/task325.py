def p(m,K=range):# floodfill n*n diag8
 r,c=len(m),len(m[0])
 def f(y,x):
  if m[y][x]:m[y][x]=0;[r>Y>-1<X<c and f(Y,X)for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1))];return 1
 n=sum(f(i,j)or 0 for i in K(r)for j in K(c));return[[8*(i==j)for j in K(n)]for i in K(n)]
