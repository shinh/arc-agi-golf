def p(g):# rot
 r=range(10);s={(i,j)for i in r for j in r if g[i][j]};a,b=zip(*s);o=min(a)+max(b)>9
 for i,j in s:g[j][9-i+o]=g[j][9-i+o]or 2
 return g
