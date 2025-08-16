def p(g):
 # spiral
 l=len(g);m=l-1;f=1;x=y=d=0;u=1,0,-1,0;v=0,1,0,-1;g[0][0]=3
 while l>0:
  for _ in[0]*(l-f):x+=u[d];y+=v[d];g[y][x]=3
  f=0;d=-~d%4
  for _ in[0]*m:x+=u[d];y+=v[d];g[y][x]=3
  d=-~d%4;l=m;m-=2
 return g
