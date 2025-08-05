def p(g):
 cnt={};c=[]
 for i in range(10):
  for j in range(10):
   if g[i][j]:
    q=[(i,j)];g[i][j]=0;o=[]
    while q:
     x,y=q.pop();o.append((x,y))
     for d in(-1,0,1):
      for e in(-1,0,1):
       if d|e:
        u,v=x+d,y+e
        if -1<u<10 and-1<v<10 and g[u][v]:
         g[u][v]=0;q.append((u,v))
    a=min(x for x,_ in o);b=min(y for _,y in o)
    s=tuple(sorted((x-a,y-b)for x,y in o));c.append((o,s));cnt[s]=cnt.get(s,0)+1
 t=min(range(len(c)),key=lambda i:cnt[c[i][1]])
 for k,(o,_) in enumerate(c):
  for i,j in o:g[i][j]=1+(k==t)
 return g
