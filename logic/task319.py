def p(g):
 # compare border mini to shapes
 f=sum(g,[]);B=max(f,key=f.count)
 O={frozenset((c,(i,j))for i,r in enumerate(g)for j,v in enumerate(r)if v==c)for c in set(f)-{B}}
 E=next(s for s in O if any(i in(0,len(g)-1)or j in(0,len(g[0])-1)for _,(i,j)in s))
 (c1,S1),(c2,S2)=[(next(iter(s))[0],[p[1]for p in s])for s in O-{E}]
 E=[p[1]for p in E]
 def m(S,c):
  R,C=zip(*S);mi,Ma=min(R),max(R);mj,Mb=min(C),max(C);S=set(S)
  return [[B+(c-B)*((i,j)in S)for j in range(mj,Mb+1)]for i in range(mi,Ma+1)]
 g1,g2,e=m(S1,c1),m(S2,c2),m(E,c1)
 return g1 if any(all(g1[(i+a)//2][(j+b)//2]==e[a][b]for a in range(len(e))for b in range(len(e[0])))for i in range(len(g1)*2-len(e)+1)for j in range(len(g1[0])*2-len(e[0])+1))else g2
