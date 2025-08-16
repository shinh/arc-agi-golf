def p(g):#frame 5-rect
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==5:
    a,b=x,y
    while len(r)>a+1and r[a+1]==5:a+=1
    while len(g)>b+1and g[b+1][a]==5:b+=1
    for R in g[y:b+1]:R[x:a+1]=[4]*-~(a-x)
    for R in g[y+1:b]:R[x+1:a]=[2]*(a-x-1)
    g[y][x]=g[y][a]=g[b][x]=g[b][a]=1
 return g
