def p(g):
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==8:R,C=i,j
 for k in range(13):
  for a,b in((R-2-2*k,C+2*k),(R+2+2*k,C-2-2*k)):
   for x,y in((a,b),(a+1,b),(a,b+1),(a,b+2)):
    if 0<=x<13 and 0<=y<13:g[x][y]=5
 if R+1<13:g[R+1][C]=5
 g[R][C]=8
 return g
