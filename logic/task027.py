def p(g):# rot
 r=range(10);s={(j,9-i)for i in r for j in r if g[i][j]};m,n=map(max,zip(*s));o=m>n
 for j,k in s:g[j][k+o]=g[j][k+o]or 2
 return g
