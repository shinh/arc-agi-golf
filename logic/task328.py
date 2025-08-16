def p(g):
 # nearest unique even-step color
 b=[r[:]for r in g]
 for y,r in enumerate(g):
  for x in range(len(r)):
   (m,k,v),(n,*_),*_=sorted((abs(y-i)+abs(x-j),~max(abs(y-i),abs(x-j))&1,v)for i,r in enumerate(b)for j,v in enumerate(r)if v)+[(99,0,0)]
   if n>m and k:r[x]=v
 return g
