def p(g):
 h=len(g);w=len(g[0])
 B=g[-1][0]  # A lucky pivot
 V=set();C=[];m=0
 for i in range(h):
  for j in range(w):
   if g[i][j]==B or(i,j)in V:continue
   q=[(i,j)];V.add((i,j));o=[]
   while q:
    a,b=q.pop();o+=((a,b),)
    for da in(-1,0,1):
     for db in(-1,0,1):
      if da|db:
       na=a+da;nb=b+db
       if 0<=na<h and 0<=nb<w and g[na][nb]!=B and(na,nb)not in V:
        V.add((na,nb));q.append((na,nb))
   k=len({g[a][b]for a,b in o})
   if k>m:m=k;C=[(g[a][b],a,b)for a,b in o]
   elif k==m:C+=[(g[a][b],a,b)for a,b in o]
 if not C:return g
 mi=min(i for _,i,_ in C);mj=min(j for _,_,j in C)
 P=[(v,(i-mi,j-mj))for v,i,j in C]
 D={}
 for v,_ in P:D[v]=D.get(v,0)+1
 x=max(D,key=D.get)
 R=[r[:]for r in g]
 for s in range(1,5):
  U=[(v,(i*s+di,j*s+dj))for v,(i,j)in P for di in range(s)for dj in range(s)]
  bh=max(i for _,(i,j)in U)+1;bw=max(j for _,(i,j)in U)+1
  Fs=(lambda i,j:(i,j),lambda i,j:(j,i),lambda i,j:(bw-1-j,bh-1-i),lambda i,j:(bh-1-i,j),lambda i,j:(i,bw-1-j))
  for t in range(5):
   f=Fs[t];hh=bw if t==1 else bh;ww=bh if t==1 else bw
   Q=[(v,f(i,j))for v,(i,j)in U];d={(i,j):v for v,(i,j)in Q if v!=x}
   if d:
    for a in range(h-hh+1):
     for b in range(w-ww+1):
      if all(g[a+i][b+j]==v for (i,j),v in d.items())and all(g[a+i][b+j]==B for i in range(hh)for j in range(ww)if(i,j)not in d):
       for v,(i,j)in Q:R[a+i][b+j]=v
 return R

