def p(g):
 # bridge shapes with 8
 d={}
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   if c:t=d.setdefault(c,[y,y,x,x]);t[:]=min(t[0],y),max(t[1],y),min(t[2],x),max(t[3],x)
 a,b=d.values();c=a[3]<b[2] or b[3]<a[2]
 if a[c*2]>b[c*2]:a,b=b,a
 s,t,u,v=[(a[1]+1,b[0],max(a[2],b[2])+1,min(a[3],b[3])),(max(a[0],b[0])+1,min(a[1],b[1]),a[3]+1,b[2])][c]
 for r in g[s:t]:r[u:v]=[8]*(v-u)
 return g
