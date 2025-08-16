def p(g):
 #max per region
 g[1:4]=[*map(max,zip(*g[1:4]))],
 for r in g:r[1:6]=max(r[1:6]),
 return g
