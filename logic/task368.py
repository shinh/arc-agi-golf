def p(g):# copy first non-05 block onto 5
 for y in range(10):
  for x in range(10):
   if g[y][x]%5:
    h=w=1
    while y+h<10 and g[y+h][x]%5:h+=1
    while x+w<10 and g[y][x+w]%5:w+=1
    for Y in range(11-h):
     for X in range(11-w):
      if g[Y][X]==5:
       for L in range(h):g[Y+L][X:X+w]=g[y+L][x:x+w]
    return g
