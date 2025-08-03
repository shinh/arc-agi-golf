def p(g):
 c=[0]*10;a=[99]*10;b=[0]*10;d=[99]*10;e=[0]*10
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:c[v]+=1;a[v]=min(a[v],y);b[v]=max(b[v],y);d[v]=min(d[v],x);e[v]=max(e[v],x)
 v=max(range(1,10),key=c.__getitem__)
 return[r[d[v]:e[v]+1]for r in g[a[v]:b[v]+1]]
