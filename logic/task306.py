def p(g):
 h,w=len(g),len(g[0]);r=range
 for y in r(h):
  for x in r(w):
   if g[y][x]:g[y%10][x%10]=g[y][x]
 return[(g[y%10][:10]*w)[:w]for y in r(h)]# tile 10x10 pattern
