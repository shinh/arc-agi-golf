def p(g):#mirror&expand blobs
 # flood fill each 3-region and mirror it horizontally with scale2, skipping rows/cols of original
 R=range;H=10
 for y in R(H):
  for x in R(H):
   if g[y][x]==3:
    q=[(y,x)];rs={y};cs={x}
    for i,j in q:
     for Y in R(i-1,i+2):
      for X in R(j-1,j+2):
       if-1<Y<H and-1<X<H and g[Y][X]==3 and(Y,X)not in q:q+=[(Y,X)];rs|={Y};cs|={X}
    my,my2=min(rs),max(rs);mx,mx2=min(cs),max(cs);h=my2-my+1;w=mx2-mx+1
    for i,j in q:
     I=2*i-my-h//2;J=2*mx2-2*j+mx-w//2
     for Y in I,I+1:
      for X in J,J+1:
       if-1<Y<H and-1<X<H and Y not in rs and X not in cs:g[Y][X]=8
 return g

