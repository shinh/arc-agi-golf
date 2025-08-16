# fill centers if edges match
def p(g):
 for k,r in enumerate(g):
  c=max(r,key=r.count)
  for i in 0,1:
   if r[i]==r[i+6]!=c:r[i+3]=r[i]
   if(t:=g[i][k])==g[i+6][k]!=c:g[i+3][k]=t
 return g
