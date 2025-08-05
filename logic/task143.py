def p(g):
 G=[r[:]for r in g];O=[];L=()
 for y in range(10):
  for x in range(10):
   if c:=G[y][x]:
    G[y][x]=0;o=q=[(y,x)];u=w=y;v=z=x
    for i,j in q:
     for A,B in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
      if 9>=A>=0<=B<=9 and G[A][B]==c:G[A][B]=0;q+=(A,B),;u=min(u,A);v=min(v,B);w=max(w,A);z=max(z,B)
    t=(c,o,u,v,w,z,{(y-u,x-v)for y,x in o});O+=t,
    if not L and len(o)==w-u+z-v+1 and not u*v*(9-w)*(9-z) and len({d for i in range(u,w+1)for d in g[i][v:z+1]})==3:L=t
 c,o,u,v,w,z,_=L;sh=next(t[6] for t in O if t[1]!=o and u<=t[2]<=w>=t[4] and v<=t[3]<=z>=t[5])
 for y,x in next(t for t in O if t[6]==sh and not(u<=t[2]<=w>=t[4] and v<=t[3]<=z>=t[5]))[1]:g[y][x]=c
 return g
