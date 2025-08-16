def p(g):
 # draw zigzags from the 8
 R,C=divmod(sum(g,[]).index(8),13)
 for k in range(0,26,2):
  for a,b in(R-2-k,C+k),(R+2+k,C-2-k):
   for x,y in(a,b),(a+1,b),(a,b+1),(a,b+2):
    if-1<x<13>y>-1:g[x][y]=5
 if R<12:g[R+1][C]=5
 return g
