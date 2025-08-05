def p(g):
 m=9**9
 for k in {x for r in g for x in r}:
  a=[r[:]for r in g]
  for t in d,c,H,V:
   b=t(a)
   for y in range(24):
    for x in range(24):
     if b[y][x]!=k:a[y][x]=b[y][x]
  s=sum(r.count(k)for r in g)
  if s<m:
   m=s;p=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==k];y0=min(i for i,_ in p);y1=max(i for i,_ in p);x0=min(j for _,j in p);x1=max(j for _,j in p);o=[r[x0:x1+1]for r in a[y0:y1+1]]
 return o
