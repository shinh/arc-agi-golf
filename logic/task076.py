def p(g):
 h=len(g);w=len(g[0])
 for y in range(h):
  for x in range(w):
   if g[y][x]&1:
    v=[*map(list,g)];a=b=y;c=d=x;S=[(y,x)]
    while S:
     y,x=S.pop()
     if-1<y<h>-1<x<w and v[y][x]:
      v[y][x]=0;a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x)
      S+=[(y+i,x+j)for i in(-1,0,1)for j in(-1,0,1)]
    U=[r[c:d+1]for r in g[a:b+1]]
    for _ in'00':
     for _ in'0000':
      H=len(U);W=len(U[0])
      for Y in range(h-H+1):
       for X in range(w-W+1):
        if all((U[i][j]&1)or g[Y+i][X+j]==U[i][j]for i in range(H)for j in range(W)):
         for i in range(H):g[Y+i][X:X+W]=U[i]
      U=[*zip(*U[::-1])]
     U=U[::-1]
    return g
 return g