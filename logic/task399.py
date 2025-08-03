def p(g):
 o=create(3,3);d=[(0,0),(0,2),(1,1),(2,0),(2,2)];c=0
 for y in range(len(g)-1):
  for x in range(len(g[0])-1):
   if g[y][x]==g[y+1][x]==g[y][x+1]==g[y+1][x+1]==2:
    i,j=d[c];o[i][j]=1;c+=1
 return o
