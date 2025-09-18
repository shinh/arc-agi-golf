def p(g):
 # dedup row/col
 return[[*zip((f:={}.fromkeys)(next(zip(*g))))],[[*f(r:=g[0])]]][len({*r})>1]
