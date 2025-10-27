def p(g):#tile diag8
 g=[r*2 for r in g]*2;t=-1,1;e=enumerate;return[[c or 8*any(g[y+d][x+e]for d in t for e in t if len(g)>y+d>-1<x+e<len(r))for x,c in e(r)]for y,r in e(g)]
