def p(g):
 _,u,v=max((sum(0<g[u+t//3][v+t%3]for t in range(9)),u,v)for u in range(19)for v in range(19))
 for a in-4,0,4:
  for b in-4,0,4:
   if c:=a|b and max(g[u+t//3+a][v+t%3+b]for t in range(9)):
    for t in range(9):
     if g[(r:=u+t//3)][(w:=v+t%3)]:
      while-1<(r:=r+a)<21 and-1<(w:=w+b)<21:g[r][w]=c
 return g
