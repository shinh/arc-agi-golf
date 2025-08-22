def p(g,d={8:4,2:1,3:6},E=enumerate):
# color neighbors
 for r,R in E(g):
  for c,C in E(R):
   for i in-1,1:
    try:H=g[r+i];H[c]=R[c+i]=H[c+i]=H[c-i]=d[C]
    except:0
 return g
