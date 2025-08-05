def p(g):
 o=[r[:]for r in g];h=10
 for y in range(h-1):
  for x in range(9):
   a=g[y][x:x+2]+g[y+1][x:x+2]
   if 0 not in a:
    for i in range(len(set(a))):
     r=y+2+i
     if r<h:o[r][x]=o[r][x+1]=3
 return o
