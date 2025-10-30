def p(g):
 # for y,r in enumerate(g)
 b=g[0][0]
 for y,r in enumerate(g):
  for x,(a,d,p) in enumerate(zip(r,r[1:],[b]+r)):
   if b!=a!=d==p!=b and r.count(p)>4:c,m=p,a
 for y,r in enumerate(g):
  for x,(a,d,p) in enumerate(zip(r,r[1:],[b]+r)):
   if a==m!=d==p!=c:u,v=y,x
 o=[*map(list,g)]
 R=range(-2,3)
 for y,r in enumerate(g):
  for x,(a,p) in enumerate(zip(r,[b]+r)):
   if a==m and p==c:
    for i in R:
     for j in R:
      if g[u+i][v+j]!=b and g[y+i][x+j]==c:o[y+i][x+j]=g[u+i][v+j]
    for i,j in((0,1),(1,0),(-1,0),(0,-1)):
     q=o[y+i][x+j]
     if q==o[y+i*2][x+j*2]:
      Y=y+i*3;X=x+j*3
      while g[Y][X]==c:o[Y][X]=q;Y+=i;X+=j
 for i in R:
  for j in R:o[u+i][v+j]=b
 return o