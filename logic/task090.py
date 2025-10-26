def p(g):
 R=range;m=len(g);n=len(g[0])
 _,a,b,c,d=max(((d-b)*(c-a),a,b,c,d)for a in R(m)for b in R(n)for c in R(a+2,m+1)for d in R(b+2,n+1)if sum(sum(y[b:d])for y in g[a:c])<1)
 for y in g[a:c]:y[b:d]=[6]*(d-b)
 return g