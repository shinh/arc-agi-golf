e=enumerate
def p(g,s=1):#rot+drop
 for _ in[0]*4:
  if s*(2in(g:=[*map(list,zip(*g[::-1]))])[0]+g[-1]):
   for r,R in e(g):
    if R[0]>7:
     for c,a in e(g[0]):
      r+=a==2;r-=g[-1][c]==2
      if-1<r<len(g):g[r][c]=8
     s=0
 return g