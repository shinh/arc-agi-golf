def p(g):
 a=g[0][0];b=g[1][1];c=g[2][2];d={a:c,b:a,c:b}
 return [[d[v]for v in r]for r in g]
