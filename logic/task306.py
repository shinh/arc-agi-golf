def p(g):
 w=len(g[0]);i=0
 for v in sum(g,[]):
  if v:g[i//w%10][i%w%10]=v
  i+=1
 return[(g[y%10][:10]*w)[:w]for y in range(len(g))]#tile 10x10
