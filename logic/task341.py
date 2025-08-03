def p(g):
 o=[r[:] for r in g];d={}
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c:d.setdefault(c,[y,y,x,x]);t=d[c];t[0]=min(t[0],y);t[1]=max(t[1],y);t[2]=min(t[2],x);t[3]=max(t[3],x)
 a,b=d.values()
 def f(s,t,u,v):
  for y in range(s,t):
   for x in range(u,v):o[y][x]=8
 if a[3]<b[2] or b[3]<a[2]:
  if a[2]>b[2]:a,b=b,a
  f(max(a[0],b[0])+1,min(a[1],b[1]),a[3]+1,b[2])
 else:
  if a[0]>b[0]:a,b=b,a
  f(a[1]+1,b[0],max(a[2],b[2])+1,min(a[3],b[3]))
 return o
