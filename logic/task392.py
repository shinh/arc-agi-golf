def p(g):
 h=10
 o=[[5]*h for _ in g]
 c=max(map(max,g))
 s={(y,x)for y in range(h)for x in range(h)if g[y][x]}
 O=[]
 while s:
  y,x=s.pop();q=[(y,x)];r={(y,x)};o[y][x]=c
  for y,x in q:
   for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
    if(Y,X)in s:s-={(Y,X)};q+=[(Y,X)];r|={(Y,X)};o[Y][X]=c
  O+=r,
 B=lambda R:(min(x for _,x in R),max(x for _,x in R),min(y for y,_ in R),max(y for y,_ in R))
 m=lambda R:max(B(R)[3]-B(R)[2],B(R)[1]-B(R)[0])
 a=min(O,key=m);O.remove(a)
 b=min(O,key=lambda R:min(abs(i-x)+abs(j-y)for i,j in R for x,y in a))
 L,R,U,D=B(a);l,r,u,d=B(b)
 H=max(r-R,L-l);V=max(d-D,U-u)
 for _ in range(15):
  U-=V;L-=H;D+=V;R+=H
  for x in range(max(L,0),min(R,9)+1):
   if 0<=U<h:o[U][x]=c
   if 0<=D<h:o[D][x]=c
  for y in range(max(U,0),min(D,9)+1):
   if 0<=L<h:o[y][L]=c
   if 0<=R<h:o[y][R]=c
 return o
