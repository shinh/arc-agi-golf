def p(g):
 b=1>(g[1][0]|g[2][0]|g[3][0])
 c=9+2*b,41+18*b
 for i in range(18):
  d=c[i>8]+(i//3%3)*9+i%3
  r=g[d//9];r[d%9]=r[d%9] or 7
 return g
