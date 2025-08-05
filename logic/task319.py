def p(g):
 h=len(g);w=len(g[0]);f=sum(g,[])
 B=max(f,key=f.count)
 O={frozenset((c,(i,j))for i,r in enumerate(g)for j,v in enumerate(r)if v==c)for c in set(f)-{B}}
 b=lambda s:any(i in(0,h-1)or j in(0,w-1)for _,(i,j)in s)
 E=next(s for s in O if b(s))
 (c1,S1),(c2,S2)=[(next(iter(s))[0],[p for _,p in s])for s in O-{E}]
 E=[p for _,p in E]
 def m(S,c):
  R,C=zip(*S);mi,Ma=min(R),max(R);mj,Mb=min(C),max(C);a=[[B]*(Mb-mj+1)for _ in range(Ma-mi+1)]
  for i,j in S:a[i-mi][j-mj]=c
  return a
 g1,g2,e=m(S1,c1),m(S2,c2),m(E,c1)
 o=lambda G,P:any(all(G[(i+a)//2][(j+b)//2]==P[a][b]for a in range(len(P))for b in range(len(P[0])))for i in range(len(G)*2-len(P)+1)for j in range(len(G[0])*2-len(P[0])+1))
 return g1 if o(g1,e)else g2
