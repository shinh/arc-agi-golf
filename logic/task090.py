def p(g):
 R=range
 _,a,b,c,d=max(((d-b)*(c-a),a,b,c,d)for a in R(len(g))for b in R(len(g[0]))for c in R(a+2,len(g)+1)for d in R(b+2,len(g[0])+1)if sum(sum(y[b:d])for y in g[a:c])<1)
 for y in g[a:c]:y[b:d]=[6]*(d-b)
 return g
