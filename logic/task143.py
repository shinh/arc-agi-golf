def p(g):
 h=len(g);w=len(g[0])
 G=[r[:]for r in g];objs=[]
 for y in range(h):
  for x in range(w):
   c=G[y][x]
   if c:
    q=[(y,x)];G[y][x]=0;o={(y,x)}
    for i,j in q:
     for a,b in((1,0),(-1,0),(0,1),(0,-1)):
      A=i+a;B=j+b
      if 0<=A<h and 0<=B<w and G[A][B]==c:G[A][B]=0;q+=[(A,B)];o.add((A,B))
    objs+=[(c,o)]
 L=None
 for c,o in objs:
  ys=[y for y,_ in o];xs=[x for _,x in o]
  sy=min(ys);sx=min(xs);ey=max(ys);ex=max(xs)
  if len(o)==ey-sy+ex-sx+1 and(sy==0 or sx==0 or ey==h-1 or ex==w-1):
   d={g[i][j]for i in range(sy,ey+1)for j in range(sx,ex+1)if(i,j)not in o}
   if len(d)==2 and(L is None or len(o)>len(L[1])):L=(c,o,sy,sx,ey,ex)
 c,o,sy,sx,ey,ex=L
 for c1,o1 in objs:
  if o1!=o and all(sy<=y<=ey and sx<=x<=ex for y,x in o1):S=o1;break
 ny=min(y for y,_ in S);nx=min(x for _,x in S)
 sh={(y-ny,x-nx)for y,x in S}
 for c1,o1 in objs:
  if o1!=S and {(y-min(y for y,_ in o1),x-min(x for _,x in o1))for y,x in o1}==sh:
   for y,x in o1:g[y][x]=c
   break
 return g
