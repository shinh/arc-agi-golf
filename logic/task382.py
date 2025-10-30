# best zopfli seed 6 -> 215 bytes
e=enumerate
def p(g,s=1):
 for _ in[0]*4:
  g=[*map(list,zip(*g[::-1]))]
  if s*(2in g[0]+g[-1]):
   for r,R in e(g):
    if R[0]:
     for c,a in e(g[0]):
      r+=(a==2)-(g[-1][c]==2)
      if-1<r<len(g):g[r][c]=8
     s=0
 return g