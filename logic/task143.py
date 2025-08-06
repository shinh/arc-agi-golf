def p(g):
 G=[*map(list,g)];O=[];L=();R=range
 for y in R(10):
  for x in R(10):
   if c:=G[y][x]:
    G[y][x]=0;o=q=[(y,x)];u=w=y;v=z=x
    for i,j in q:
     for A,B in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
      if -1<A<10>B>-1 and G[A][B]==c:G[A][B]=0;q+=(A,B),;u=min(u,A);v=min(v,B);w=max(w,A);z=max(z,B)
    q=o,u,v,w,z,{(y-u,x-v)for y,x in o};O+=q,
    if not L and len(o)==w-u+z-v+1 and u*v*(9-w)*(9-z)<1 and len({d for i in R(u,w+1)for d in g[i][v:z+1]})>2:L=q;C=c
 o,u,v,w,z,_=L;B=lambda t:u<=t[1]<=w>=t[3] and v<=t[2]<=z>=t[4];sh=next(t[5] for t in O if t!=L and B(t))
 for y,x in next(t for t in O if t[5]==sh and not B(t))[0]:g[y][x]=C
 return g
