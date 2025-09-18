def p(g):
 # fill max empty rect w/6
 h,w,r=len(g),len(g[0]),range
 _,a,b,c,d=max(((d-b)*(c-a),a,b,c,d)for a in r(h)for b in r(w)for c in r(a+2,h+1)for d in r(b+2,w+1)
  if sum(e for y in g[a:c]for e in y[b:d])<1)
 for y in g[a:c]:y[b:d]=[6]*(d-b)
 return g

