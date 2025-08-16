def p(g):
 # expand the smallest blob at constant offsets
 c=max(map(max,g));o=[[5]*10for _ in g]
 s={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v};O=[]
 while s:
  q=[s.pop()]
  for y,x in q:
   o[y][x]=c
   for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
    if(Y,X)in s:s.remove((Y,X));q+=[(Y,X)]
  O+=q,
 a=min(O,key=lambda R:(lambda Y,X:max(max(Y)-min(Y),max(X)-min(X)))(*zip(*R)));O.remove(a)
 b=min(O,key=lambda R:min(abs(i-x)+abs(j-y)for i,j in R for x,y in a))
 Y,X=zip(*a);U,D,L,R=min(Y),max(Y),min(X),max(X);Y,X=zip(*b)
 H=max(max(X)-R,L-min(X));V=max(max(Y)-D,U-min(Y))
 for _ in[0]*15:
  U-=V;L-=H;D+=V;R+=H
  for x in range(L,R+1):
   for y in U,D:
    if-1<y<10 and-1<x<10:o[y][x]=c
  for y in range(U,D+1):
   for x in L,R:
    if-1<y<10 and-1<x<10:o[y][x]=c
 return o
