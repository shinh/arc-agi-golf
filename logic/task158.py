def p(g):# BFS region then copy scaled
 h=len(g);w=len(g[0]);B=g[-1][0];v=set();R=range
 for y in R(h):
  for j in R(w):
   if g[y][j]==B or(y,j)in v:continue
   q=[(y,j)];v|={(y,j)}
   for a,b in q:
    for dy in-1,0,1:
     for dx in-1,0,1:
      if dy|dx and-1<(ny:=a+dy)<h>-1<(nx:=b+dx)<w and g[ny][nx]!=B and(ny,nx)not in v:
       q+=[(ny,nx)];v|={q[-1]}
   if len({g[i][j]for i,j in q})<2:continue
   y,x=map(min,zip(*q));P=[(g[i][j],i-y,j-x)for i,j in q]
   c,I,J=zip(*P);m=max(c,key=c.count);h0=max(I)+1;w0=max(J)+1
   for s in R(1,5):
    U=[(c,i*s+di,j*s+dj)for c,i,j in P for di in R(s)for dj in R(s)];H=h0*s;W=w0*s
    for t in R(5):
     q=[(v,(i,j,j,i,W-1-j,H-1-i,H-1-i,j,i,W-1-j)[t*2:][:2])for v,i,j in U]
     d={(i,j):v for v,(i,j)in q if v!=m}
     if d:
      hh,ww=[(H,W),(W,H)][t==1]
      for a in R(h-hh+1):
       for b in R(w-ww+1):
        if all(g[a+i][b+j]==d.get((i,j),B)for i in R(hh)for j in R(ww)):
         for v,(i,j)in q:g[a+i][b+j]=v
   return g
 return g
