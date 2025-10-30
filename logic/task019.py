def p(g):#tile diag8
 g=[r*2 for r in g]*2;E=enumerate;return[[c or 8*any(g[y+d][x+e]for d in(-1,1)for e in(-1,1)if len(g)>y+d>-1<x+e<len(r))for x,c in E(r)]for y,r in E(g)]
