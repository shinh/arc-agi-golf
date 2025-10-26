def p(g):
 # tile diag8
 g=[r*2 for r in g]*2;h=len(g);w=len(g[0]);t=-1,1
 return[[g[y][x]or 8*any(g[y+d][x+e]for d in t for e in t if h>y+d>-1<x+e<w)for x in range(w)]for y in range(h)]
