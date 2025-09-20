def p(j):
 # mark 1..4 diagonals around 2x2 5s
 for y in range(len(j)-1):
  for x in range(len(j[0])-1):
   if j[y][x:x+2]==j[y+1][x:x+2]==[5]*2:j[y-1][x-1:x+3:3]=1,2;j[y+2][x-1:x+3:3]=3,4
 return j
