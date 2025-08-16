def p(g):
 # draw upward lines from bottom 2s, shifting right past 5s
 for j,x in enumerate(g[-1]):
  if x>1:
   y=0
   for r in g[::-1]:
    if r[j]>4:j+=1;g[-y][j]=2
    r[j]=2;y+=1
 return g

