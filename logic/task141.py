def p(g):
 y=-1
 for r in g:
  y+=1;x=-1
  for v in r:
   x+=1
   if v:c=v;a=y-x;b=y+x
 h=len(g);w=len(g[0]);o=create(h,w)
 for y in range(h):
  for x in range(w):
   if y-x==a or y+x==b:o[y][x]=c
 return o
