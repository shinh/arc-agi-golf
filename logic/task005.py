def p(g):
 # repeat largest blob toward hint
 n=21;D=-1,0,1;E=[(a,b)for a in D for b in D if a|b];e=max(g[0]);t=[r[:]for r in g];B=[];R=range(n)
 def f(y,x):
  if-1<y<n>-1<x and t[y][x]==c:
   t[y][x]=e;S.append((y,x))
   for a,b in E:f(y+a,x+b)
 for y in R:
  for x in R:
   c=t[y][x]
   if c-e:S=[];f(y,x);len(S)>len(B)and(B:=S)
 Y,X=zip(*B);h=max(Y)+1-min(Y);w=max(X)+1-min(X)
 for dy,dx in E:
  sy=(h+1)*dy;sx=(w+1)*dx;C=e
  for y,x in B:
   u=y+sy;v=x+sx
   if-1<u<n and-1<v<n and g[u][v]-e:C=g[u][v];break
  k=0
  while C-e:
   k+=1;f=0
   for y,x in B:
    u=y+sy*k;v=x+sx*k
    if-1<u<n and-1<v<n:g[u][v]=C;f=1
   if f<1:break
 return g
