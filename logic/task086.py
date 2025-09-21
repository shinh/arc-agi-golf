def p(g):# flood fill then expand
 h=len(g);w=len(g[0]);o=[r[:]for r in g];r=range
 for i in r(h):
  for j in r(w):
   if a:=g[i][j]:
    b=0;g[i][j]=0;s=[(i,j)];m=M=i;l=R=j
    for y,x in s:
     for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
      if h>Y>-1<X<w and (t:=g[Y][X]):
       g[Y][X]=0;s+=(Y,X),;m=min(m,Y);M=max(M,Y);l=min(l,X);R=max(R,X);t!=a and(b:=t)
    P=M-m;Q=R-l
    for y,x in s:
     for Y,X in(y-P+1,x),(y+P-1,x),(y,x-Q+1),(y,x+Q-1):
      if h>Y>-1<X<w:o[Y][X]=a
    for y in r(m,M+1):o[y][l:R+1]=[a]*-~Q;o[y][l]=o[y][R]=b
    o[m][l:R+1]=o[M][l:R+1]=[b]*-~Q
 return o
