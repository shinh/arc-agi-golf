# fill square interiors by size parity
def p(g):
 for i in range(len(g)-1):
  a,b=g[i:i+2]
  for j in range(len(a)-1):
   if a[j]==b[j]==a[j+1]==1>b[j+1]:
    s=[(n:=(a+[0])[j:].index(0))%2*5+2]*(n-2)
    for m in range(n-2):g[i+m+1][j+1:j+n-1]=s
 return g
