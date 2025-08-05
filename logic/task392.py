def p(g):
 o=[[5]*10 for _ in g]
 c=max(sum(g,[]))
 s={(y,x)for y in range(10)for x in range(10)if g[y][x]}
 O=[]
 while s:
  y,x=s.pop();q=[(y,x)];r={(y,x)};o[y][x]=c
  for y,x in q:
   for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
    if(Y,X)in s:s.remove((Y,X));q+=[(Y,X)];r|={(Y,X)};o[Y][X]=c
  O+=r,
 a=min(O,key=lambda R:(lambda Y,X:max(max(Y)-min(Y),max(X)-min(X)))(*zip(*R)));O.remove(a)
 b=min(O,key=lambda R:min(abs(i-x)+abs(j-y)for i,j in R for x,y in a))
 Y,X=zip(*a);U,D,L,R=min(Y),max(Y),min(X),max(X);Y,X=zip(*b);u,d,l,r=min(Y),max(Y),min(X),max(X)
 H=max(r-R,L-l);V=max(d-D,U-u)
 for _ in range(15):
  U-=V;L-=H;D+=V;R+=H
  for x in range(max(L,0),min(R,9)+1):
   if 0<=U<10:o[U][x]=c
   if 0<=D<10:o[D][x]=c
  for y in range(max(U,0),min(D,9)+1):
   if 0<=L<10:o[y][L]=c
   if 0<=R<10:o[y][R]=c
 return o

