def p(g):
 h=len(g);w=len(g[0])
 for r,row in enumerate(g):
  for c,v in enumerate(row):
   if v:
    for j in range(h-1,0,-1):g[j]=g[j-1][:]
    pat=[4*(i%2==c%2) for i in range(w)]
    for i in range(r+1):g[i]=pat[:]
    return g
