def p(g):
 # stripes
 w=len(g[0]);y1,x1,c1,y2,x2,c2=sum(((y,x,g[y][x])for y in range(len(g))for x in range(w)if g[y][x]),())
 b=x1*x2<1 or x1==x2 or y1*y2>0>=abs(x1-x2)-abs(y1-y2)
 if not b:
  g=[*zip(*g)];w=len(g[0]);y1,x1,y2,x2=x1,y1,x2,y2
 if y1>y2:y1,x1,c1,y2,x2,c2=y2,x2,c2,y1,x1,c1
 d=y2-y1;g[y1::2*d]=[[c1]*w]*len(g[y1::2*d]);g[y2::2*d]=[[c2]*w]*len(g[y2::2*d])
 return([*map(list,zip(*g))],g)[b]
