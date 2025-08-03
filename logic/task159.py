def p(g):
 h=len(g);w=len(g[0])
 sx=w;sy=h;ex=ey=0
 px=py=w;qx=qy=0
 for y in range(h):
  for x in range(w):
   v=g[y][x]
   if v==2:
    if x<sx:sx=x
    if y<sy:sy=y
    if x>ex:ex=x
    if y>ey:ey=y
   elif v:
    if x<px:px=x
    if y<py:py=y
    if x>qx:qx=x
    if y>qy:qy=y
 n=ex-sx+1;k=(n-2)//(qy-py+1)
 o=[[0]*n for _ in range(n)]
 for i in range(n):o[0][i]=o[-1][i]=o[i][0]=o[i][-1]=2
 for y in range(py,qy+1):
  for x in range(px,qx+1):
   v=g[y][x]
   if v:
    for dy in range(k):
     for dx in range(k):o[1+(y-py)*k+dy][1+(x-px)*k+dx]=v
 return o
