def p(g):
 # nearest unique even-step color
 e=enumerate;a=abs;s=[(i,j,v)for i,r in e(g)for j,v in e(r)if v]
 for y,r in e(g):
  for x,_ in e(r):
   m=min((a(y-i)+a(x-j),~max(a(y-i),a(x-j))&1,v)for i,j,v in s)
   if m[1]==sum(a(y-i)+a(x-j)==m[0]for i,j,_ in s)==1:r[x]=m[2]
 return g
