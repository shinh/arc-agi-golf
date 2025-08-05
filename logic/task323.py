def p(g):
 h=len(g);w=len(g[0])
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==8:R,C=i,j
 for k in range(max(h,w)):
  for a,b in((R-2-2*k,C+2*k),(R+2+2*k,C-2-2*k)):
   for x,y in((a,b),(a+1,b),(a,b+1),(a,b+2)):
    if 0<=x<h and 0<=y<w:g[x][y]=5
 if R+1<h:g[R+1][C]=5
 g[R][C]=8
 return g
