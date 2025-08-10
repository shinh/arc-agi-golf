def p(g):
 h=len(g);w=len(g[0]);B=g[-1][0];v=set()
 for y in range(h):
  for j in range(w):
   if g[y][j]==B or(y,j)in v:continue
   q=[(y,j)];v|={(y,j)}
   for a,b in q:
    for dy in-1,0,1:
     for dx in-1,0,1:
      if dy|dx:
       ny=a+dy;nx=b+dx
       if-1<ny<h and-1<nx<w and g[ny][nx]!=B and(ny,nx)not in v:
        v|={(ny,nx)};q+=[(ny,nx)]
   if len({g[i][j]for i,j in q})<2:continue
   y=min(i for i,_ in q);x=min(j for _,j in q);P=[(g[i][j],i-y,j-x)for i,j in q]
   L=[q[0]for q in P];m=max(L,key=L.count)
   h0=max(i for _,i,_ in P)+1;w0=max(j for _,_,j in P)+1;R=[r for r in g]
   for s in 1,2,3,4:
    U=[(c,i*s+di,j*s+dj)for c,i,j in P for di in range(s)for dj in range(s)];H=h0*s;W=w0*s
    for t in range(5):
     q=[(v,(i,j,j,i,W-1-j,H-1-i,H-1-i,j,i,W-1-j)[t*2:t*2+2])for v,i,j in U]
     d={(i,j):v for v,(i,j)in q if v!=m}
     if d:
      hh,ww=[(H,W),(W,H)][t==1]
      for a in range(h-hh+1):
       for b in range(w-ww+1):
        if all(g[a+i][b+j]==d.get((i,j),B)for i in range(hh)for j in range(ww)):
         for v,(i,j)in q:R[a+i][b+j]=v
   return R
 return g
