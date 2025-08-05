def p(g):
 h=len(g);w=len(g[0])
 t=sum(g,[]);c=min({*t},key=t.count)
 S={(y,x)for y in range(h)for x in range(w)if g[y][x]==c}
 s=0
 while s-len(S):
  s=len(S)
  for y in range(h):
   xs=[x for x in range(w)if(y,x)in S]
   for a,b in zip(xs,xs[1:]):
    if b-a<5:S|={(y,x)for x in range(a+1,b)}
  for x in range(w):
   ys=[y for y in range(h)if(y,x)in S]
   for a,b in zip(ys,ys[1:]):
    if b-a<5:S|={(y,x)for y in range(a+1,b)}
 T={(y,x)for y,x in S if{(y-1,x),(y+1,x)}&S and{(y,x-1),(y,x+1)}&S}
 L=0;M=set()
 for y in range(h):
  x=0
  while x<w:
   if(y,x)in S:
    z=x
    while z<w and(y,z)in S:z+=1
    d=z-x
    if d>L:L=d;M=set()
    if d==L and all((y-1,t)not in S and(y+1,t)not in S for t in range(x,z)):M.add((y,x+d//2))
    x=z
   x+=1
 for x in range(w):
  y=0
  while y<h:
   if(y,x)in S:
    z=y
    while z<h and(z,x)in S:z+=1
    d=z-y
    if d>L:L=d;M=set()
    if d==L and all((t,x-1)not in S and(t,x+1)not in S for t in range(y,z)):M.add((y+d//2,x))
    y=z
   y+=1
 T|=M;m=L//2
 for y,x in T:
  for d in range(-m,m+1):
   if 0<=y+d<h:S.add((y+d,x))
   if 0<=x+d<w:S.add((y,x+d))
 for y,x in S:g[y][x]=(8,c)[g[y][x]==c]
 return g
