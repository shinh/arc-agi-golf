def p(g):
 _,u,v=max((sum(g[u+t//3][v+t%3]>0for t in range(9)),u,v)for u in range(19)for v in range(19))
 for a in-4,0,4:
  for b in-4,0,4:
   if a|b and(c:=max(g[u+t//3+a][v+t%3+b]for t in range(9))):
    for t in range(9):
     if g[u+t//3][v+t%3]:
      r=u+t//3+a;w=v+t%3+b
      while-1<r<21>w>-1:g[r][w]=c;r+=a;w+=b
 return g
