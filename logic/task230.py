def p(j):
 # mark diagonals 1..4 around 2x2 block of 5s
 for y in range(len(j)-1):
  for x in range(len(j[0])-1):
   if 5==j[y][x]==j[y][x+1]==j[y+1][x]==j[y+1][x+1]:
    j[y-1][x-1]=1;j[y-1][x+2]=2;j[y+2][x-1]=3;j[y+2][x+2]=4
 return j
