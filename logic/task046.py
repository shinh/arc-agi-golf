def p(g):
 h=len(g);w=len(g[0])
 f=sum(g,[])
 d={(i,j):v for i,r in enumerate(g) for j,v in enumerate(r)if v};o=[]
 while d:
  q=[next(iter(d))];u=[]
  for x,y in q:
   if(x,y)in d:
    v=d.pop((x,y));u+=[(v,x,y)]
    q+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
  o+=u,
 s=[c for c in set(f)if all(1<=sum(v==c for v,_,_ in u)<=2 for u in o)]
 sp=min(s,key=f.count)
 o.sort(key=lambda u:min(y for _,_,y in u))
 r=[];a=None
 for u in o:
  spc=[(i,j)for v,i,j in u if v==sp];oth=[(v,i,j)for v,i,j in u if v!=sp]
  col=[v for v,_,_ in oth];m=max(col+[0],key=col.count)
  if a==None:r+=oth+[(m,i,j)for i,j in spc];a=max(spc);continue
  ac=min(spc,key=lambda p:(abs(p[0]-a[0])+abs(p[1]-a[1]),p[1],p[0]))
  di=a[0]-ac[0];dj=a[1]-ac[1]+1
  spc=[(i+di,j+dj)for i,j in spc];oth=[(v,i+di,j+dj)for v,i,j in oth];ac=(ac[0]+di,ac[1]+dj)
  r+=oth+[(m,i,j)for i,j in spc]
  spc=[p for p in spc if p!=ac];a=max(spc)if spc else ac
 if not r:return g
 mi=min(j for _,_,j in r);ma=max(j for _,_,j in r);w=ma-mi+1
 out=[[0]*w for _ in g]
 for v,i,j in r:
  j-=mi
  if 0<=i<h and 0<=j<w:out[i][j]=v
 return out

