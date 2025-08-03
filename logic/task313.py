def p(g):
 f=g[-1][-1];r=g[0];w=r.index(f) if f in r else len(r);t=r[:w]
 for p in range(1,w+1):
  if all(t[i]==t[i%p] for i in range(w)):break
 c=t[:p];H=len(g);W=len(r)
 return [[c[(1+(y&1)+x)%p] for x in range(W)] for y in range(H)]
