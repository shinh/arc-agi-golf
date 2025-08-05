def p(g):
 for y,r in enumerate(g):
  if 4 in r:x=r.index(4);break
 a=y//4*4;b=x//4*4;c=y%4*4;d=x%4*4
 o=[[5*(v==5)for v in r]for r in g]
 for i in range(3):o[c+i][d:d+3]=g[a+i][b:b+3]
 return o

