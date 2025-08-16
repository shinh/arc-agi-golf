def p(g,A=range):# copy first non-05 block onto 5
 c=len(g)
 for y in A(c):
  for x in A(c):
   if g[y][x]%5:
    h=w=1
    while y+h<c and g[y+h][x]%5:h+=1
    while x+w<c and g[y][x+w]%5:w+=1
    for Y in A(c-h+1):
     for X in A(c-w+1):
      if g[Y][X]==5:
       for L in A(h):g[Y+L][X:X+w]=g[y+L][x:x+w]
    return g
