def p(g):
 s=sum(g,[]);L=[(),()]
 for y,r in enumerate(g):
  if 5 in r:
   for x in range(r.index(5)+1,9-r[::-1].index(5)):
    if not s[i:=y*10+x]:L[y//5]+=i,
 t=[sum(1<<(x-f[0])for x in f)for f in L]
 for k in {*s}-{0,5}:
  q=[i for i,a in enumerate(s)if a==k];x=sum(1<<(i-q[0])for i in q)
  if x in t:
   for i in q:g[i//10][i%10]=0
   for i in L[t.index(x)]:g[i//10][i%10]=k
 return g