def p(g):
 s=sum(g,[]);l=[(),()]
 for y,r in enumerate(g):
  if 5in r:
   for x in range(r.index(5)+1,9-r[::-1].index(5)):
    if not s[i:=y*10+x]:l[y>4]+=i,
 d={tuple(x-f[0]for x in f):f for f in l}
 for k in{*s}-{0,5}:
  q=[i for i,a in enumerate(s)if a==k]
  if f:=d.get(tuple(i-q[0]for i in q)):
   for i in q:g[i//10][i%10]=0
   for i in f:g[i//10][i%10]=k
 return g
