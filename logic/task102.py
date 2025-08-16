def p(g):
 # fill square holes
 for y in range(12):
  for x in range(12):
   if g[y][x]<1:
    q=[(y,x)];g[y][x]=1
    for y1,x1 in q:
     for y2,x2 in((y1-1,x1),(y1+1,x1),(y1,x1-1),(y1,x1+1)):
      if-1<y2<12 and-1<x2<12 and g[y2][x2]<1:g[y2][x2]=1;q+=[(y2,x2)]
    ys,xs=zip(*q);a=min(ys);b=max(ys);c=min(xs);d=max(xs)
    c=2 if b-a==d-c==len(q)**.5-1 and all(g[a-1][i]==g[b+1][i]==5 for i in range(c,d+1)) and all(g[i][c-1]==g[i][d+1]==5 for i in range(a,b+1)) else 0
    for y1,x1 in q:g[y1][x1]=c
 return g
