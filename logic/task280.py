def p(g):
 for _ in[0]*4:
  for y,r in enumerate(g):
   n=w=0
   for x,c in enumerate(r):
    n+=c>2
    if c<1:
     if w:
      for z in g[y-n:y+n+1]:z[x]=3
      g[y][x]=2
     n*=w
    w*=c<3;w|=c==2
  g=[*map(list,zip(*g[::-1]))]
 return g
