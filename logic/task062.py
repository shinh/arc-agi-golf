def p(g):
 d=sum(r.count(2)for r in g)
 for _ in[0]*4:
  g=[*zip(*g)][::-1]
  for r in range(10):
   t=g[r]
   if sum(t)==t.count(2)*2==d*2:
    for y in range(10-r):
     t=g[r+y];i=r-y+1
     if sum(t)>t.count(2)*2 and 0<=i<10:g[i]=t
 return [[c or 3 for c in r]for r in g]
