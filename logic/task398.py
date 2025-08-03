def p(g):
 r=g[0];n=5*sum(v>0 for v in r);o=create(n,n);r=r+[0]*(n-5)
 for i in range(n):
  o[n-1-i]=r[:n];r=[0]+r[:-1]
 return o
