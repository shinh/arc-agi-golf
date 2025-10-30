def p(g):
 for i in range(10):
  for j in range(10):
   if g[i][j]%5:
    h=w=1
    while i+h<10 and g[i+h][j]%5:h+=1
    while j+w<10 and g[i][j+w]%5:w+=1
    for y in range(10):
     for x in range(10):
      if g[y][x]==5:
       for k in range(h):g[y+k][x:x+w]=g[i+k][j:j+w]
    return g