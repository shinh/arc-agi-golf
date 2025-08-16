# fill below nonzero 2x2 blocks with 3
R=range(9)

def p(g):
 o=eval(str(g))
 for y in R:
  for x in R:
   for r in o[y+2:][:all(a:=g[y][x:x+2]+g[y+1][x:x+2])*len({*a})]:r[x:x+2]=3,3
 return o
