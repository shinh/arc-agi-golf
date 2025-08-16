def p(g):#mirror&expand blobs
 R=range;H=10
 for y in R(H):
  for x in R(H):
   if g[y][x]==3:
    q=[(y,x)];rs=[y];cs=[x]
    for i,j in q:
     for Y in R(i-1,i+2):
      for X in R(j-1,j+2):
       if-1<Y<H and-1<X<H and g[Y][X]==3 and(Y,X)not in q:q+=[(Y,X)];rs+=[Y];cs+=[X]
    my,my2=min(rs),max(rs);mx,mx2=min(cs),max(cs);h=my2-my+1;w=mx2-mx+1
    for i,j in q:
     for a in 0,1:
      I=(i-my)*2+a+my-h//2
      for b in 0,1:
       J=(mx2-j)*2+b+mx-w//2
       if-1<I<H and-1<J<H and I not in rs and J not in cs:g[I][J]=8
 return g
