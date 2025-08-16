def p(g):
 # nearest unique even-step color
 c=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v]
 for y,r in enumerate(g):
  for x in range(len(r)):
   d=sorted((abs(y-a)+abs(x-b),a,b,v)for a,b,v in c)+[(9e9,)*4];m,a,b,v=d[0];
   if d[1][0]>m and ~max(abs(y-a),abs(x-b))&1:r[x]=v
 return g
