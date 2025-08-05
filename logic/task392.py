def p(g):
 h=10
 o=[[5]*h for _ in g]
 c=next(v for r in g for v in r if v)
 s={(y,x)for y in range(h)for x in range(h)if g[y][x]==c}
 O=[]
 while s:
  y,x=s.pop();q=[(y,x)];r={(y,x)};o[y][x]=c
  while q:
   y,x=q.pop()
   for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
    if(Y,X)in s:s-={(Y,X)};q+=[(Y,X)];r|={(Y,X)};o[Y][X]=c
  O+=r,
 r=lambda R:max(x for _,x in R);l=lambda R:min(x for _,x in R);u=lambda R:min(y for y,_ in R);d=lambda R:max(y for y,_ in R)
 m=lambda R:max(d(R)-u(R),r(R)-l(R))
 a=min(O,key=m);O.remove(a)
 f=lambda R:min(abs(i-x)+abs(j-y)for i,j in R for x,y in a)
 b=min(O,key=f)
 H=max(r(b)-r(a),l(a)-l(b));V=max(d(b)-d(a),u(a)-u(b))
 U,L0,D0,R0=u(a),l(a),d(a),r(a)
 for n in range(1,16):
  T=U-V*n;L=L0-H*n;D=D0+V*n;R=R0+H*n
  for x in range(max(L,0),min(R,9)+1):
   if 0<=T<h:o[T][x]=c
   if 0<=D<h:o[D][x]=c
  for y in range(max(T,0),min(D,9)+1):
   if 0<=L<h:o[y][L]=c
   if 0<=R<h:o[y][R]=c
 return o
