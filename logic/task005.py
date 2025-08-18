def p(g):
 # repeat biggest 3x3 block indicated by hints
 e=max(g[0]);B=[];m=0
 for y in range(19):
  for x in range(19):
   t=[]
   for i in range(3):
    for j in range(3):
     if g[y+i][x+j]!=e:t.append((y+i,x+j))
   if len(t)>m:m=len(t);B=t
 for dy in -1,0,1:
  for dx in -1,0,1:
   if dy|dx:
    sy=4*dy;sx=4*dx;c=e
    for y,x in B:
     u=y+sy;v=x+sx
     if 0<=u<21 and 0<=v<21 and g[u][v]!=e:c=g[u][v];break
    k=0
    while c!=e:
     k+=1;f=0
     for y,x in B:
      u=y+sy*k;v=x+sx*k
      if 0<=u<21 and 0<=v<21:g[u][v]=c;f=1
     if f<1:break
 return g
