def p(g):
 #spread
 for _ in[0]*4:
  for e in[r.index(8)for r in g if 8in r]:
   for r in g:
    f=n=0
    for x in range(e):
     if(c:=r[x]):n or f and(n:=c)or(f:=c)
     elif n:r[x-1:e+1]=[n]*(e-x)+[n,f];n=0
  g[:]=map(list,zip(*g[::-1]))
 return g
