def p(g):# fill inside 5 square
 for s in 3,4,5:
  for y in range(13-s):
   for x in range(13-s):
    if all(5==g[y][x+i]==g[y+s-1][x+i]==g[y+i][x]==g[y+i][x+s-1]for i in range(s)):
     for i in range(s-2):g[y+i+1][x+1:x+s-1]=[s+3]*(s-2)
 return g
