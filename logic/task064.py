def p(g):
 # extend segments via rotations
 b=max(r:=g[0],key=r.count)
 for _ in[0]*4:
  for r in g:
   for x,c in enumerate(r):
    if(c-b)*(x<1or r[x-1]==b)*(b in r[x+1:x+3]):
     for j,u in enumerate(r[x:-1],x):
      if b!=u==r[j+1]!=c:r[x:j]=[c]*(j-x);break
  g=[*map(list,zip(*g[::-1]))]
 return g
