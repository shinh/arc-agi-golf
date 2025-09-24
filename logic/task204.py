# fill square interiors by size parity
def p(g):
 for i,(a,b) in enumerate(zip(g,g[1:])):
  for j in range(len(a)-1):
   if b[j+1]<1==a[j]==a[j+1]==b[j]:
    for r in g[i+1:i+(n:=(a+[0])[j:].index(0))-1]:r[j+1:j+n-1]=[(n&1)*5+2]*(n-2)
 return g
