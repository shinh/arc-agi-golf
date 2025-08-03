def p(g):
 t=None;w=len(g[0])
 for y,r in enumerate(g):
  if not any(r):continue
  k=w
  while k and r[k-1]==0:k-=1
  if k==w:t=r
  else:
   T=[];[T.append(x)for x in t if x not in T]
   P=[];[P.append(x)for x in r[:k] if x not in P]
   m={T[i]:P[i] for i in range(len(P))}
   g[y]=[m.get(x,0) for x in t];t=g[y]
 return g
