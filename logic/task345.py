def p(g):
 # draw upward lines from bottom 2s, shifting right past 5s
 for j,x in enumerate(g[-1]):
  if x:
   for r,b in[*zip(g,g[1:])][::-1]:b[j:=j+(r[j]>4)]=2;r[j]=2
 return g

