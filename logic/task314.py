# fill centers if edges match
def p(g):
 for k,r in enumerate(g):
  for i in 0,1:
   if(c:=max(r,key=r.count))!=r[i]==r[i+6]:r[i+3]=r[i]
   if(t:=g[i][k])==g[i+6][k]!=c:g[i+3][k]=t
 return g
