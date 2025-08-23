# fill below nonzero 2x2 blocks with 3

def p(g):
 for i in range(81):
  y=8-i//9;x=i%9
  for r in g[y+2:][:all(a:=g[y][x:x+2]+g[y+1][x:x+2])*len({*a})]:r[x:x+2]=3,3
 return g
