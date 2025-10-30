def p(g):# rot
 s={(k%10,9-k//10)for k,v in enumerate(sum(g,[]))if v};m,n=map(max,zip(*s));o=m>n
 for j,k in s:g[j][k+o]=g[j][k+o]or 2
 return g
