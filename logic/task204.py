def p(g):
 H=len(g);W=len(g[0])
 for y in range(H):
  for x in range(W):
   if g[y][x]==0:
    s=[(y,x)];g[y][x]=-1;mY=M=y;mX=N=x;b=y in(0,H-1)or x in(0,W-1)
    for i,j in s:
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=i+dy,j+dx
      if 0<=ny<H and 0<=nx<W and g[ny][nx]==0:
       g[ny][nx]=-1;s.append((ny,nx))
       if ny in(0,H-1)or nx in(0,W-1):b=1
       mY=min(mY,ny);M=max(M,ny);mX=min(mX,nx);N=max(N,nx)
    h=M-mY+1;w=N-mX+1;c=0
    if not b and h==w and len(s)==h*w:c=[7,2][h%2<1]
    for i,j in s:g[i][j]=c
 return g
