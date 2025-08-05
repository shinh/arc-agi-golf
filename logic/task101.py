def p(g):
 h=len(g);w=len(g[0]);P=(-1,0,1);V=set();C=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]and(y,x)not in V:
    q=[(y,x)];V.add((y,x));S=[];col=set()
    for Y,X in q:
     S+=[(Y,X)];col|={g[Y][X]}
     for a in P:
      for b in P:
       if a|b:
        y2=Y+a;x2=X+b
        if 0<=y2<h and 0<=x2<w and g[y2][x2]and(y2,x2)not in V:V.add((y2,x2));q+=[(y2,x2)]
    C+=[(S,col)]
 T=[s for s,c in C if 1 in c and 2 in c][0]
 A=[p for p in T if g[p[0]][p[1]]==2];B=[p for p in T if g[p[0]][p[1]]==1]
 my=min(y for y,_ in A);mx=min(x for _,x in A)
 A=[(y-my,x-mx)for y,x in A];B=[(y-my,x-mx)for y,x in B];U=A+B
 mnx=min(x for _,x in U);mxx=max(x for _,x in U)
 mny=min(y for y,_ in U);mxy=max(y for y,_ in U)
 P=[]
 for k in range(1,min(h,w)+1):
  for y in range(h):
   for x in range(w):
    ok=1
    for a,b in A:
     for dy in range(k):
      for dx in range(k):
       Y=y+a*k+dy;X=x+b*k+dx
       if not(0<=Y<h and 0<=X<w and g[Y][X]==2):ok=0;break
      if not ok:break
     if not ok:break
    if ok:
     for a,b in B:
      for dy in range(k):
       for dx in range(k):
        Y=y+a*k+dy;X=x+b*k+dx
        if 0<=Y<h and 0<=X<w and g[Y][X]:ok=0;break
       if not ok:break
      if not ok:break
    if ok:
     S={(y+a*k+dy,x+b*k+dx)for a,b in A for dy in range(k)for dx in range(k)}
     for Y in range(y+mny*k,y+(mxy+1)*k):
      for X in range(x+mnx*k,x+(mxx+1)*k):
       if 0<=Y<h and 0<=X<w and g[Y][X]==2 and (Y,X)not in S:ok=0;break
      if not ok:break
     if ok:P+=[(y,x,k)]
 for y,x,k in P:
  for a,b in B:
   for dy in range(k):
    for dx in range(k):
     Y=y+a*k+dy;X=x+b*k+dx
     if 0<=Y<h and 0<=X<w and g[Y][X]!=2:g[Y][X]=1
 return g

