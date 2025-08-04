def p(g):
 h=len(g);w=len(g[0])
 d={}
 for r in g:
  for v in r:d[v]=d.get(v,0)+1
 bg=max(d,key=d.get)
 seen=set();comps=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==bg or (i,j)in seen:continue
   s=[(i,j)];seen.add((i,j));c=[]
   while s:
    a,b=s.pop();c.append((a,b))
    for da in(-1,0,1):
     for db in(-1,0,1):
      if da|db:
       na=a+da;nb=b+db
       if 0<=na<h and 0<=nb<w and g[na][nb]!=bg and (na,nb)not in seen:
        seen.add((na,nb));s.append((na,nb))
   comps.append(c)
 m=0;best=[]
 for c in comps:
  l=len({g[i][j]for i,j in c})
  if l>m:m=l;best=[c]
  elif l==m:best+=c,
 cells=[(g[i][j],i,j)for c in best for i,j in c]
 if not cells:return g
 mi=min(i for _,i,_ in cells);mj=min(j for _,_,j in cells)
 p=[(v,(i-mi,j-mj))for v,i,j in cells]
 d={}
 for v,_ in p:d[v]=d.get(v,0)+1
 x=max(d,key=d.get)
 r=[row[:]for row in g]
 def tf(p,h,w,t):
  if t==1:return[(v,(j,i))for v,(i,j)in p]
  if t==2:return[(v,(w-1-j,h-1-i))for v,(i,j)in p]
  if t==3:return[(v,(h-1-i,j))for v,(i,j)in p]
  if t==4:return[(v,(i,w-1-j))for v,(i,j)in p]
  return p
 for s in range(1,5):
  u=[(v,(i*s+di,j*s+dj))for v,(i,j)in p for di in range(s)for dj in range(s)]
  bh=max(i for _,(i,j)in u)+1;bw=max(j for _,(i,j)in u)+1
  for t in range(5):
   q=tf(u,bh,bw,t)
   mi=min(i for _,(i,j)in q);mj=min(j for _,(i,j)in q)
   q=[(v,(i-mi,j-mj))for v,(i,j)in q]
   idx={(i,j):v for v,(i,j)in q if v!=x}
   if not idx:continue
   hh=max(i for _,(i,j)in q)+1;ww=max(j for _,(i,j)in q)+1
   for a in range(h-hh+1):
    for b in range(w-ww+1):
     if all(g[a+i][b+j]==v for (i,j),v in idx.items()) and all(g[a+i][b+j]==bg for i in range(hh) for j in range(ww) if (i,j)not in idx):
      for v,(i,j) in q:r[a+i][b+j]=v
 return r
