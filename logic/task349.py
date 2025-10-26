def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==9 and (i<1 or g[i-1][j]-9)and(j<1 or g[i][j-1]-9):
    w=1
    while j+w<len(g[0]) and g[i][j+w]==9:w+=1
    h=1
    while i+h<len(g) and g[i+h][j]==9:h+=1
    r=w//2
    for y in range(i+h,len(g)):
     for x in range(j,j+w):g[y][x]=max(g[y][x],1)
    for y in range(i-r,i+h+r):
     if 0<=y<len(g):
      for x in range(j-r,j+w+r):
       if 0<=x<len(g[0]):g[y][x]=max(g[y][x],3)
 return g