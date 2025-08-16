def p(g):
 # bridge shapes with 8
 d={}
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c:
    t=d.setdefault(c,[y,y,x,x]);t[:2]=min(t[0],y),max(t[1],y);t[2:]=min(t[2],x),max(t[3],x)
 a,b=d.values()
 if a[3]<b[2] or b[3]<a[2]:
  if a[2]>b[2]:a,b=b,a
  s,t,u,v=max(a[0],b[0])+1,min(a[1],b[1]),a[3]+1,b[2]
 else:
  if a[0]>b[0]:a,b=b,a
  s,t,u,v=a[1]+1,b[0],max(a[2],b[2])+1,min(a[3],b[3])
 for y in range(s,t):g[y][u:v]=[8]*(v-u)
 return g
