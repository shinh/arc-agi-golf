def p(g):
 R=range(6)
 r=c=0
 while g[r][c]<1:c+=1;c%=6;r+=c<1
 return[[g[r+(i<r)][c+(j<c)]if((-3<i-r<0)+(1<i-r<4))*((-3<j-c<0)+(1<j-c<4))else g[i][j]for j in R]for i in R]