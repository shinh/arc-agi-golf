def p(C,Y=range):
 n=len(C)
 b=[[0 for _ in Y(n)]for _ in Y(n)]
 for i in Y(n):
  for j in Y(n):
   if C[i][j]==5:
    for x in Y(max(0,i-1),min(n,i+2)):
     for y in Y(max(0,j-1),min(n,j+2)):b[x][y]=1
 return b