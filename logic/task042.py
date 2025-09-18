def p(g):#mirror&expand blobs
 # flood 3 blobs & mirror off their rows/cols
 R=range(10)
 for y in R:
  for x in R:
   if g[y][x]==3:
    q=[(y,x)]
    for i,j in q:
     for Y in i-1,i,i+1:
      for X in j-1,j,j+1:
       if-1<Y<10>-1<X<10>g[Y][X]==3 and(Y,X)not in q:q+=[(Y,X)]
    a,b=zip(*q);m,M=min(a),max(a);n,N=min(b),max(b)
    c=m+M+1>>1;d=2*N+n-(N-n+1>>1)
    for i,j in q:
     i=2*i-c;j=d-2*j
     for Y in i,i+1:
      for X in j,j+1:
       if-1<Y<10>-1<X<10>(Y in a)+(X in b)<1:g[Y][X]=8
 return g
