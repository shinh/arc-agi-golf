def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):d.setdefault(v,[]).append((i,j))
 def c(a):
  is_=[i for i,_ in a];js=[j for _,j in a]
  return(min(is_)+max(is_))//2,(min(js)+max(js))//2
 t=lambda b,p:(b[0]+(p[0]>b[0])-(p[0]<b[0]),b[1]+(p[1]>b[1])-(p[1]<b[1]))
 b=0
 o=[r for r in g]
 for v in(3,7):
  for i,j in d.get(v,[]):o[i][j]=b
 if 1 in d:
  b1=c(d[1])
  for p2 in d.get(7,[]):i,j=t(b1,p2);o[i][j]=7
 if 2 in d:
  b2=c(d[2])
  for p2 in d.get(3,[]):i,j=t(b2,p2);o[i][j]=3
 return o
