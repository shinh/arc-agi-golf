def p(g,A=enumerate):#bar
 for y,r in A(g):
  for x,v in A(r):
   if~4&v:
    for R in g[:y+1]:R[x&1::2]=[4]*len(R[x&1::2])
    g[y+1][x]=v;return g
