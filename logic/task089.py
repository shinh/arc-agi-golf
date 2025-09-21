def p(g):# clone 3 blob & mirror 2 blob
 R=range(13)
 v=[];o2=o3=l2=l3=0
 for y in R:
  for x in R:
   if(y,x)not in v and(c:=g[y][x]):
    q=o=[(y,x,c)];s={c}
    for y,x,c in q:
     v+=[(y,x)];s|={c}
     for a in-1,0,1:
      for b in-1,0,1:
       if a|b and-1<(Y:=y+a)<13 and-1<(X:=x+b)<13 and(Y,X)not in v and(C:=g[Y][X]):q+=[(Y,X,C)]
    t=len(s);3 in s and t>l3 and(o3:=o,l3:=t);2 in s and t>l2 and(o2:=o,l2:=t)
 def app(k,o,orig=()):
  ay=min(y for y,x,c in o if c==k);ax=min(x for y,x,c in o if c==k)
  for y in R:
   for x in R:
    if g[y][x]==k and(y,x)not in orig:
     for Y,X,c in o:
      if-1<(Y:=y+Y-ay)<13 and-1<(X:=x+X-ax)<13:g[Y][X]=c
 o3 and app(3,o3)
 if o2:mn,mx=sorted(x for y,x,_ in o2)[::len(o2)-1];app(2,[(y,mx-x+mn,c)for y,x,c in o2],{(y,x)for y,x,c in o2 if c==2})
 return g

