def p(g):
 t=sum(g,[])
 L=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if t.count(v)<3]
 c=[*zip(*g)]
 for x in{*t}:
  d=[0,0]
  for i,j in L:d[(x in g[i])&(x in c[j])^1]=g[i][j]
  if t.count(x)>2 and 0 not in d:break
 return [[(v,d[(x in g[i])&(x in c[j])^1])[any((i+j==p+q)|(i-j==p-q)for p,q in L)]for j,v in enumerate(r)]for i,r in enumerate(g)]