def p(g):
 r=c=0;R=range(6)
 while g[r][c]<1:c=-~c%6;r+=c<1
 return[[(g[r+(i<r)][c+(j<c)],g[i][j])[i-r&j-c&2<1]for j in R]for i in R]
