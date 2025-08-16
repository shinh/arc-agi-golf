def p(g):#mirror&expand blobs
 H=W=10;R=range
 v=set()
 for y in R(H):
  for x in R(W):
   if g[y][x]==3 and(y,x)not in v:
    q=[(y,x)];p=[];rs=set();cs=set()
    for i,j in q:
     if(i,j)in v:continue
     v.add((i,j));p+=[(i,j)];rs.add(i);cs.add(j)
     for Y in R(i-1,i+2):
      for X in R(j-1,j+2):
       if-1<Y<H and-1<X<W and g[Y][X]==3:q.append((Y,X))
    my,my2=min(rs),max(rs);mx,mx2=min(cs),max(cs);h=my2-my+1;w=mx2-mx+1
    for i,j in p:
     for a in 0,1:
      I=(i-my)*2+a+my-h//2
      for b in 0,1:
       J=(mx2-j)*2+b+mx-w//2
       if-1<I<H and-1<J<W and I not in rs and J not in cs:g[I][J]=8
 return g
