def p(g):
 for x in range(15):
   n=0
   while g[15-1-n][x]:
    c=g[14-n][x]
    g[14-n][x]=0
    n+=1
   for i in range(n):
    g[14-n-i][x]=c
 return g