def p(g):# clone 3 blob & mirror 2 blob
 d=[(a,b)for a in(-1,0,1)for b in(-1,0,1)if a|b];R=range(13)
 v=[];o2=o3=l2=l3=0
 for y in R:
  for x in R:
   if g[y][x]and(y,x)not in v:
    q=o=[(y,x,c:=g[y][x])];s={c}
    for y,x,c in q:
     v+=[(y,x)];s|={c}
     for a,b in d:
      Y=y+a;X=x+b
      if 13>Y>-1<X<13 and g[Y][X]and(Y,X)not in v:q+=[(Y,X,g[Y][X])]
    t=len(s);3 in s and t>l3 and(o3:=o,l3:=t);2 in s and t>l2 and(o2:=o,l2:=t)
 def app(k,o,orig=()):
  ay=min(y for y,x,c in o if c==k);ax=min(x for y,x,c in o if c==k)
  p=[(c,y-ay,x-ax)for y,x,c in o]
  for y in R:
   for x in R:
    if g[y][x]==k and(y,x)not in orig:
     for c,dy,dx in p:
      Y=y+dy;X=x+dx
      if 13>Y>-1<X<13:g[Y][X]=c
 o3 and app(3,o3)
 if o2:mn,mx=sorted(x for y,x,_ in o2)[::len(o2)-1];app(2,[(y,mx-x+mn,c)for y,x,c in o2],{(y,x)for y,x,c in o2 if c==2})
 return g

