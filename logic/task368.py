def p(g):# copy block to 5
 r=range
 for y in r(10):
  for x in r(10):
   if g[y][x]%5:
    h=w=1
    while y+h<10 and g[y+h][x]%5:h+=1
    while x+w<10 and g[y][x+w]%5:w+=1
    for Y in r(11-h):
     for X in r(11-w):
      if g[Y][X]==5:
       for L in r(h):g[Y+L][X:X+w]=g[y+L][x:x+w]
    return g
