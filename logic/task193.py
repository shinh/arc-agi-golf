def p(g):
 h=len(g);w=len(g[0])
 o=[r[:] for r in g]
 hr=[[0]*w for _ in g]
 for y,r in enumerate(g):
  x=0
  while x<w:
   c=r[x]
   if c:
    x2=x
    while x2<w and r[x2]==c:x2+=1
    for i in range(x,x2):hr[y][i]=x2-x
    x=x2
   else:x+=1
 vr=[[0]*w for _ in g]
 for x in range(w):
  y=0
  while y<h:
   c=g[y][x]
   if c:
    y2=y
    while y2<h and g[y2][x]==c:y2+=1
    for i in range(y,y2):vr[i][x]=y2-y
    y=y2
   else:y+=1
 for y in range(h):
  for x in range(w):
   if o[y][x] and not((hr[y][x]>2 and vr[y][x]>1) or (hr[y][x]>1 and vr[y][x]>2)):
    o[y][x]=0
 return o
