# swap 2 next to 3 with 0 and 8
def p(g,e=enumerate):
 for i,r in e(g):
  for j,v in e(r):
   for x,y in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
    if v==2and g[x:x+1]and g[x][y:y+1]==[3]:r[j]=0;g[x][y]=8
 return g
