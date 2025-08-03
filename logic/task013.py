def p(g):
 h=len(g);w=len(g[0]);a=[(y,x,g[y][x])for y in range(h)for x in range(w)if g[y][x]];y1,x1,c1=a[0];y2,x2,c2=a[1]
 dx=abs(x1-x2);dy=abs(y1-y2)
 if x1==0 or x2==0 or x1==x2 or y1 and y2 and dx<=dy:
  if y1>y2:y1,x1,c1,y2,x2,c2=y2,x2,c2,y1,x1,c1
  d=y2-y1;s=[c1]+[0]*~-d+[c2]+[0]*~-d;t=(s*(h//len(s)+1))[:h-y1]
  for i,v in enumerate(t):g[y1+i]=[v]*w
 else:
  if x1>x2:y1,x1,c1,y2,x2,c2=y2,x2,c2,y1,x1,c1
  d=x2-x1;s=[c1]+[0]*~-d+[c2]+[0]*~-d;t=(s*(w//len(s)+1))[:w-x1]
  for r in g:r[x1:]=t
 return g
