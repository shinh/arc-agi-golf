def p(g):
 d={};y=-1
 for r in g:
  y+=1;x=-1
  for v in r:
   x+=1
   if v:d.setdefault(v,[]).append((y,x))
 ys,xs=zip(*min(d.values(),key=len))
 return [r[min(xs):max(xs)+1] for r in g[min(ys):max(ys)+1]]
