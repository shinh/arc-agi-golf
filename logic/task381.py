def p(g):
 # fill zeros between outer 2s
 for r in g[1:-1]:
  if 2 in r:
   i=r.index(2)+1;j=~r[::-1].index(2);r[i:j]=[v or 9 for v in r[i:j]]
 return g
