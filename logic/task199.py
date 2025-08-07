def p(g,R=range,r=0):
 for row in g:
  r+=1
  c=1
  for v in row:
   c=1-c
   if v:
    for j in R(len(g)-1,0,-1):g[j]=g[j-1]
    pat=[4*(i%2==c) for i in R(len(g[0]))]
    for i in R(r):g[i]=pat
    return g
