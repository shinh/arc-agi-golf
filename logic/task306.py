def p(g):
 w=len(g[0])
 for i,v in enumerate(sum(g,[])):
  if v:g[i//w%10][i%w%10]=v
 return[(g[y%10][:10]*w)[:w]for y in range(len(g))]# tile 10x10 pattern
