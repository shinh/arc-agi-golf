def p(g):
 # nearest unique even-step color
 e=enumerate;a=abs;b=eval(str(g))
 for y,r in e(g):
  for x,_ in e(r):
   (m,k,v),(n,*_),*_=sorted((a(y-i)+a(x-j),~max(a(y-i),a(x-j))&1,v)for i,r in e(b)for j,v in e(r)if v)+[(99,0,0)]
   if k*n>m:r[x]=v
 return g
