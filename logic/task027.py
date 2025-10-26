def p(g):
 s={(i,j)for i in range(10)for j in range(10)if g[i][j]};o=s|{(9-j,i)for i,j in s}!=s|{(j,9-i)for i,j in s}
 for i,j in s:g[j][9-i+o]=g[j][9-i+o]or 2
 return g