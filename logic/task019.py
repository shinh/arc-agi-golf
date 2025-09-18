def p(g):
 # tile grid and add 8s diagonally
 h=len(g);w=len(g[0]);t=-1,1;R=range
 return [[g[y%h][x%w]or 8*any(g[(y+d)%h][(x+e)%w]for d in t for e in t if -1<y+d<h*2>-1<x+e<w*2) for x in R(w*2)]for y in R(h*2)]

