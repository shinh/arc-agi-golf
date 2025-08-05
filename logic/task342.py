def p(g):
 h=w=10;o=create(h,w)
 for y in range(h-1):
  for x in range(w-1):
   if g[y][x]==g[y+1][x]==g[y][x+1]==g[y+1][x+1]==8:r,c=y,x
 for y in range(h):
  for x in range(w):
   v=g[y][x]
   if v and v-8:
    if y<r:
     if x<c:o[r][c]=v
     elif x>c+1:o[r][c+1]=v
    elif y>r+1:
     if x<c:o[r+1][c]=v
     elif x>c+1:o[r+1][c+1]=v
 return o
