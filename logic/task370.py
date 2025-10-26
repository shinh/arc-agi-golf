def p(g):
 h=len(g);w=len(g[0])
 for a in 1,-1:
  for b in 1,-1:
   for s in range(1,h+w):
    C=0;q=1
    for x in range(h):
     for y in range(w):
      if g[x][y]<1:
       i,j=x+a*s,y+b*s
       if-1<i<h and-1<j<w:
        v=g[i][j]
        q&=v>0
        if v-g[0][0]:C=v
    if q and C:
     for m in range(1,h+w):
      for x in range(h):
       for y in range(w):
        if g[x][y]<1:
         i,j=x+a*m*s,y+b*m*s
         if-1<i<h and-1<j<w:g[i][j]=C
     return g