def p(g):# draw upward lines from bottom 2s, shifting right past 5s
 for j,x in enumerate(g[-1]):
  for r,b in[*zip(g,g[1:])][::-1]*(x>>1):j+=r[j]>4;b[j]=r[j]=2
 return g

