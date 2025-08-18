def p(g):
 # expand color cells to their surrounding frame of 1's
 for y in range(10):
  for x in range(10):
   c=g[y][x]
   if c>1:
    l=x
    while g[y][l]!=1:l-=1
    r=x
    while g[y][r]!=1:r+=1
    u=y
    while u and 1 in g[u-1][l:r+1]:u-=1
    d=y
    while d<9 and 1 in g[d+1][l:r+1]:d+=1
    for i in range(u and u-1,d+1):
     R=g[i]
     for j in range(l,r+1):
      if R[j]!=1:R[j]=c
 return g
