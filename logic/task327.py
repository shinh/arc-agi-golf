def p(g):
 o=create(6,6)
 for y in range(6):
  for x in range(6):
   d=y-x
   if d>0:
    for c in range(min(x,2),-1,-1):
     r=c+d
     if r<3 and g[r][c]:o[y][x]=g[r][c];break
   else:
    for r in range(min(y,2),-1,-1):
     c=r-d
     if c<3 and g[r][c]:o[y][x]=g[r][c];break
 return o
