def p(g):
 #max per region
 return[(r[0],max(r[1:6]),r[6])for r in(g[0],[*map(max,*g[1:4])],g[4])]
