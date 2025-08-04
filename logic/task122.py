def p(g):
 h=len(g);w=len(g[0]);C={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):C.setdefault(v,set()).add((i,j))
 def B(s):i,j=zip(*s);return min(i),max(i),min(j),max(j)
 bg=max(C,key=lambda k:(lambda t,b,l,r:(b-t+1)*(r-l+1))(*B(C[k])))
 a,b=[k for k in C if k!=bg]
 def F(k):
  S=C[k]
  for i,j in S:
   if{(i+1,j),(i-1,j),(i,j+1),(i,j-1)}&S:return k
 p=F(a)or b
 L=C[a^b^p];P=C[p]
 t=min(L,key=sum)
 o=min([q for q in L if q!=t],key=lambda q:abs(q[0]-t[0])+abs(q[1]-t[1]))
 di=(len({i for i,_ in L})>1)*abs(o[0]-t[0])
 dj=(len({j for _,j in L})>1)*abs(o[1]-t[1])
 R=[r[:]for r in g]
 for i,j in P:R[i][j]=bg
 for i,j in {(i+di,j+dj)for i,j in P}:
  if 0<=i<h and 0<=j<w:R[i][j]=p
 return R

