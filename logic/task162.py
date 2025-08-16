def p(g,R=range(18)):
 # fill blank 3x3 squares with ones
 for i in R:
  a,b,c=g[i:i+3]
  for j in R:
   if sum(a[j:(k:=j+3)]+b[j:k]+c[j:k])<1:a[j:k]=b[j:k]=c[j:k]=[1]*3
 return g