def p(g):
 o=[[5]*10 for _ in g]
 c=max(map(max,g))
 s={(y,x)for y in range(10)for x in range(10)if g[y][x]}
 O=[]
 while s:
  y,x=s.pop();q=[(y,x)];r={(y,x)};o[y][x]=c
  for y,x in q:
   for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
    if(Y,X)in s:s.remove((Y,X));q+=[(Y,X)];r|={(Y,X)};o[Y][X]=c
  O+=r,
 B=lambda R:(min(x for _,x in R),max(x for _,x in R),min(y for y,_ in R),max(y for y,_ in R))
 a=min(O,key=lambda R:max(B(R)[3]-B(R)[2],B(R)[1]-B(R)[0]));O.remove(a)
 b=min(O,key=lambda R:min(abs(i-x)+abs(j-y)for i,j in R for x,y in a))
 L,R,U,D=B(a);l,r,u,d=B(b)
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

