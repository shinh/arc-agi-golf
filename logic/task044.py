def p(g):
 s=sum(g,[]);L=[(),()];p=-9;d=-1
 for y,r in enumerate(g):
  if 5 in r:
   d+=y>p+1;p=y;a=r.index(5)+1
   for x in range(a,9-r[::-1].index(5)):
    if not s[i:=y*10+x]:L[d]+=i,
 m={tuple(x-min(f)for x in f):f for f in L}
 for k in {*s}-{0,5}:
  q=[i for i,v in enumerate(s)if v==k];t=tuple(x-min(q)for x in q)
  if t in m:
   for i in q:g[i//10][i%10]=0
   for i in m[t]:g[i//10][i%10]=k
 return g
