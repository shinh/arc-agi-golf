def p(g):
 d=lambda a:[list(r)for r in zip(*a)]
 c=lambda a:[list(r)for r in zip(*[r[::-1]for r in a[::-1]])]
 H=lambda a:[r[:]for r in a[::-1]]
 V=lambda a:[r[::-1]for r in a]
 m=9**9
 for k in {x for r in g for x in r}:
  a=[r[:]for r in g]
  for t in d,c,H,V:
   b=t(a)
   for y in range(24):
    for x in range(24):
     if b[y][x]!=k:a[y][x]=b[y][x]
  if a==H(a)==V(a)==d(a)==c(a):
   s=sum(r.count(k)for r in g)
   if s<m:
    m=s;p=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==k];y0=min(i for i,_ in p);y1=max(i for i,_ in p);x0=min(j for _,j in p);x1=max(j for _,j in p);o=[r[x0:x1+1]for r in a[y0:y1+1]]
 return o
