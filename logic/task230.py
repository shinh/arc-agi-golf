def p(j):
 r=range(len(j)-1)
 for i in r:
  for k in r:
   if j[i][k]*j[i][k+1]*j[i+1][k]:j[i-1][k-1:k+3:3]=1,2;j[i+2][k-1:k+3:3]=3,4
 return j