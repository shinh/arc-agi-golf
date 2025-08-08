def p(g):
 d=[(a,b)for a in(-1,0,1)for b in(-1,0,1)if a|b]
 v=set();o2=o3=l2=l3=0
 for y in range(13):
  for x in range(13):
   if g[y][x]and(y,x)not in v:
    q=[(y,x)];o=[];s=set()
    while q:
     y,x=q.pop();v.add((y,x));c=g[y][x];o+=[(y,x,c)];s.add(c)
     for a,b in d:
      Y=y+a;X=x+b
      if 0<=Y<13 and 0<=X<13 and g[Y][X]and(Y,X)not in v:q+=[(Y,X)]
    t=len(s)
    if 3 in s and t>l3:o3=o;l3=t
    if 2 in s and t>l2:o2=o;l2=t
 out=[r for r in g]
 def app(k,o,orig=()):
  ay=min(y for y,x,c in o if c==k);ax=min(x for y,x,c in o if c==k)
  p=[(c,y-ay,x-ax)for y,x,c in o]
  for y in range(13):
   for x in range(13):
    if g[y][x]==k and(y,x)not in orig:
     for c,dy,dx in p:
      Y=y+dy;X=x+dx
      if 0<=Y<13 and 0<=X<13:out[Y][X]=c
 if o3:app(3,o3)
 if o2:
  mn=min(x for y,x,_ in o2);mx=max(x for y,x,_ in o2)
  o=[(y,mx-x+mn,c)for y,x,c in o2]
  app(2,o,{(y,x)for y,x,c in o2 if c==2})
 return out

