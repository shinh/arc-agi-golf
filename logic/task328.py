def p(g):
 h=len(g);w=len(g[0]);b=0
 c=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v]
 for y in range(h):
  for x in range(w):
   d=sorted((abs(y-a)+abs(x-b),a,b,v)for a,b,v in c);(m,a,b,v)=d[0];n=d[1][0]if len(d)>1 else 99
   if m<n and max(abs(y-a),abs(x-b))%2<1:g[y][x]=v
 return g
