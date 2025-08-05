def p(g):
 h=len(g);w=len(g[0]);B=g[-1][0]
 V=set();C=[];m=0
 for i in range(h):
  for j in range(w):
   if g[i][j]==B or(i,j)in V:continue
   q=[(i,j)];V.add((i,j));o=[];s=set()
   while q:
    a,b=q.pop();o+=((a,b),);s.add(g[a][b])
    for da in-1,0,1:
     for db in-1,0,1:
      if da|db:
       na=a+da;nb=b+db
       if-1<na<h and-1<nb<w and g[na][nb]!=B and(na,nb)not in V:
        V.add((na,nb));q+=[(na,nb)]
   k=len(s)
   if k>=m:
    if k>m:m=k;C=[]
    C+=[(g[a][b],a,b)for a,b in o]
 if not C:return g
 mi=min(i for _,i,_ in C);mj=min(j for _,_,j in C)
 P=[(v,(i-mi,j-mj))for v,i,j in C];D={}
 for v,_ in P:D[v]=D.get(v,0)+1
 x=max(D,key=D.get)
 if len(D)==1:return g
 h0=max(i for _,(i,j)in P)+1;w0=max(j for _,(i,j)in P)+1
 R=[r[:]for r in g]
 for s in 1,2,3,4:
  U=[(v,(i*s+di,j*s+dj))for v,(i,j)in P for di in range(s)for dj in range(s)]
  bh=h0*s;bw=w0*s
  for t in 0,1,2,3,4:
   q=[(v,((i,j),(j,i),(bw-1-j,bh-1-i),(bh-1-i,j),(i,bw-1-j))[t])for v,(i,j)in U]
   d={(i,j):v for v,(i,j)in q if v!=x}
   if d:
    hh,ww=(bw,bh)if t==1 else(bh,bw)
    for a in range(h-hh+1):
     for b in range(w-ww+1):
      if all(g[a+i][b+j]==d.get((i,j),B)for i in range(hh)for j in range(ww)):
       for v,(i,j)in q:R[a+i][b+j]=v
 return R
