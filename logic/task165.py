def p(g):
 # rotate to match shape then drop rare color
 s={18,9,15,3,11,21,27,16,19,10}
 R=lambda a:[list(x)for x in zip(*a[::-1])]
 G=g
 for un in 4,3,2,1:
  for pc in range(10):
   P={(i,j)for i,r in enumerate(G)for j,v in enumerate(r)if v==pc}
   if P:
    mi,mj=map(min,zip(*P))
    if {(i-mi)*7+j-mj for i,j in P}==s:break
  else:G=R(G);continue
  break
 l=sum(G,[])
 m=min(set(l)-{pc},key=l.count)
 for j in{j for i,r in enumerate(G)for j,v in enumerate(r) if v==m and any((k,j)in P for k in range(i))}:
  b=max(i for i,k in P if k==j)+1
  for r in G[b:]:r[j]=m
 for _ in(0,)*un:G=R(G)
 return G
