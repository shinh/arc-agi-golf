def p(g):
 c=next(v for r in g for v in r if v)
 P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
 a=min(i for i,_ in P);b=min(j for _,j in P)
 s=[r[b:b+9]for r in g[a:a+9]]
 t=[[s[i][j]for j in(0,3,6)]for i in(0,3,6)]
 Q=[(i,j)for i,r in enumerate(t)for j,v in enumerate(r)if v==c]
 o=[[0]*9 for _ in range(9)]
 for x,y in Q:
  for u,v in Q:o[x*3+u][y*3+v]=c
 return o
