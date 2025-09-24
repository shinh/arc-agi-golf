def p(g):
 # draw zigzags from the 8
 R,C=divmod(sum(g,[]).index(8),13)
 for t in range(2,28,2):
  for d in-1,1:
   for x,y in((a:=R+d*t),(b:=C-d*t+d-1)),(a+1,b),(a,b+1),(a,b+2):
    if-1<x<13>y>-1:g[x][y]=5
 if R<12:g[R+1][C]=5
 return g
