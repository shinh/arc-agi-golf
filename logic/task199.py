def p(g,A=enumerate):#stripe
 for y,r in A(g):
  for x,v in A(r):
   if 0<v!=4:
    for R in g[:y+1]:R[x&1::2]=[4]*len(R[x&1::2])
    g[y+1][x]=v;return g
