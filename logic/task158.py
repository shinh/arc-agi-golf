def p(g):
 h=len(g);w=len(g[0])
 d={}
 for r in g:
  for v in r:d[v]=d.get(v,0)+1
 bg=max(d,key=d.get)
 v=[[0]*w for _ in g];o=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=bg and not v[i][j]:
    s=[(i,j)];v[i][j]=1;c=[]
    while s:
     a,b=s.pop();c.append((g[a][b],a,b))
     for da in(-1,0,1):
      for db in(-1,0,1):
       if da or db:
        na=a+da;nb=b+db
        if 0<=na<h and 0<=nb<w and g[na][nb]!=bg and not v[na][nb]:
         v[na][nb]=1;s.append((na,nb))
    o.append(c)
 m=0;u=[]
 for q in o:
  c=len({x for x,_,_ in q})
  if c>m:m=c;u=[q]
  elif c==m:u+=q,
 t=[(x,i,j)for q in u for x,i,j in q]
 if not t:return g
 mi=min(i for _,i,_ in t);mj=min(j for _,_,j in t)
 p=[(x,(i-mi,j-mj))for x,i,j in t]
 d={}
 for x,_ in p:d[x]=d.get(x,0)+1
 x=max(d,key=d.get)
 r=[row[:]for row in g]
 def f(p,h,w,t):
  if t==1:return[(v,(j,i))for v,(i,j)in p],w,h
  if t==2:return[(v,(w-1-j,h-1-i))for v,(i,j)in p],w,h
  if t==3:return[(v,(h-1-i,j))for v,(i,j)in p],h,w
  if t==4:return[(v,(i,w-1-j))for v,(i,j)in p],h,w
  return p[:],h,w
 for s in range(1,5):
  u=[(v,(i*s+di,j*s+dj))for v,(i,j)in p for di in range(s)for dj in range(s)]
  bh=max(i for _,(i,j)in u)+1;bw=max(j for _,(i,j)in u)+1
  for t in range(5):
   q,hp,wp=f(u,bh,bw,t)
   mi=min(i for _,(i,j)in q);mj=min(j for _,(i,j)in q)
   q=[(v,(i-mi,j-mj))for v,(i,j)in q]
   non=[(v,(i,j))for v,(i,j)in q if v!=x]
   if not non:continue
   idx={(i,j):v for v,(i,j)in non}
   hh=max(i for _,(i,j)in q)+1;ww=max(j for _,(i,j)in q)+1
   for a in range(h-hh+1):
    for b in range(w-ww+1):
     for (i,j),v in idx.items():
      if g[a+i][b+j]!=v:break
     else:
      ok=1
      for i2 in range(hh):
       for j2 in range(ww):
        if (i2,j2)not in idx and g[a+i2][b+j2]!=bg:ok=0;break
       if not ok:break
      if ok:
       for v,(i3,j3)in q:r[a+i3][b+j3]=v
 return r
