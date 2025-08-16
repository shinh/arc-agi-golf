def p(g):
 # repeat largest blob toward hint
 n=21;D=-1,0,1;e=max(g[0])
 t=[r[:]for r in g];B=[]
 def f(i,j):
  if 0<=i<n>j>=0 and t[i][j]==c:
   t[i][j]=e;S.append((i,j))
   for a in D:
    for b in D:
     if a|b:f(i+a,j+b)
 for y in range(n):
  for x in range(n):
   c=t[y][x]
   if c!=e:
    S=[];f(y,x)
    if len(S)>len(B):B=S
 Y,X=zip(*B);h=max(Y)-min(Y)+1;w=max(X)-min(X)+1
 for dy in D:
  for dx in D:
   if dy|dx:
    sy=(h+1)*dy;sx=(w+1)*dx;C=e
    for y,x in B:
     u=y+sy;v=x+sx
     if 0<=u<n>v>=0 and g[u][v]!=e:C=g[u][v];break
    k=0
    while C!=e:
     k+=1;f=0
     for y,x in B:
      u=y+sy*k;v=x+sx*k
      if 0<=u<n>v>=0:g[u][v]=C;f=1
     if not f:break
 return g
