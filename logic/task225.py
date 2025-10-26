def p(g):
 r=c=0;R=range(6)
 while g[r][c]<1:c=-~c%6;r+=c<1
 return[[g[i][j]if(i-r)%4<2or(j-c)%4<2else g[r+(i<r)][c+(j<c)]for j in R]for i in R]