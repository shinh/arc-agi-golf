def p(g):
 h=len(g);w=len(g[0])
 r=[all(c==0 for c in row)for row in g]
 c=[all(g[y][x]==0 for y in range(h))for x in range(w)]
 for y in range(h):
  for x in range(w):
   if r[y]or c[x]:g[y][x]=2
 return g
