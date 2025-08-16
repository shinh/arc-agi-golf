def p(g):
 # find most common color, crop its bbox
 c=[0]*10
 for v in sum(g,[]):c[v]+=v>0
 v=c.index(max(c))
 a=d=99;b=e=0
 for y,r in enumerate(g):
  for x,u in enumerate(r):
   if u==v:a=min(a,y);b=max(b,y);d=min(d,x);e=max(e,x)
 return[r[d:e+1]for r in g[a:b+1]]
