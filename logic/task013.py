def p(g):
 # stripes
 h=len(g);w=len(g[0]);y1,x1,c1,y2,x2,c2=sum([(y,x,g[y][x])for y in range(h)for x in range(w)if g[y][x]],())
 if x1*x2<1 or x1==x2 or y1*y2 and abs(x1-x2)<=abs(y1-y2):
  if y1>y2:y1,x1,c1,y2,x2,c2=y2,x2,c2,y1,x1,c1
  d=y2-y1;s=[c1]+[0]*~-d+[c2]+[0]*~-d;t=(s*(h//len(s)+1))[:h-y1]
  g[y1:]=[[v]*w for v in t]
 else:
  if x1>x2:y1,x1,c1,y2,x2,c2=y2,x2,c2,y1,x1,c1
  d=x2-x1;s=[c1]+[0]*~-d+[c2]+[0]*~-d;t=(s*(w//len(s)+1))[:w-x1]
  for r in g:r[x1:]=t
 return g
