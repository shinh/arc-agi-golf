def p(g):
 s=sum(g,[]);M=[];p=-9
 for y,r in enumerate(g):
  if 5 in r:
   if not M or y>p+1:M+=(),
   p=y
   for x in range(r.index(5)+1,9-r[::-1].index(5)):
    if not s[i:=y*10+x]:M[-1]+=i,
 m={tuple(x-f[0]for x in f):f for f in M}
 for k in {*s}-{0,5}:
  q=[i for i,v in enumerate(s)if v==k]
  if f:=m.get(tuple(x-q[0]for x in q)):
   for i in q:g[i//10][i%10]=0
   for i in f:g[i//10][i%10]=k
 return g
