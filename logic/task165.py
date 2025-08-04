def p(g):
 S={(2,4),(1,2),(2,1),(0,3),(1,4),(3,0),(3,6),(2,2),(2,5),(1,3)}
 r=lambda a:[list(x)for x in zip(*a[::-1])]
 R=[(lambda x:x,lambda x:x),(r,lambda x:r(r(r(x)))),(lambda x:r(r(x)),lambda x:r(r(x))),(lambda x:r(r(r(x))),r)]
 for A,B in R:
  t=A(g)
  for c in range(10):
   pts=[(i,j)for i,row in enumerate(t)for j,v in enumerate(row)if v==c]
   if pts:
    mi=min(i for i,_ in pts);mj=min(j for _,j in pts)
    if {(i-mi,j-mj)for i,j in pts}==S:
     G=A([r[:]for r in g]);pc=c;un=B;break
  else:continue
  break
 pal={v for row in G for v in row};pal.discard(pc)
 m=min(pal,key=lambda c:sum(row.count(c)for row in G))
 P={(i,j)for i,row in enumerate(G)for j,v in enumerate(row)if v==pc}
 pts=[(i,j)for i,row in enumerate(G)for j,v in enumerate(row)if v==m]
 cols={j for i,j in pts if any((k,j)in P for k in range(i))}
 H=len(G)
 for j in cols:
  b=max(i for i,k in P if k==j)+1
  for i in range(b,H):G[i][j]=m
 return un(G)
