def p(g):
 g=[*map(list,g)]
 # use bounding box to fill slanted arms
 t,*_,B=[i for i,x in enumerate(g)if any(x)];l,*_,r=[i for i,x in enumerate(zip(*g))if any(x)]
 if all(g[t][l:r+1]):return [*zip(*p([*zip(*g[::-1])]))][::-1]
 for i in range(B):
  h=g[i]
  for c in range(l+1+(i<=t),r-(i<=t)):h[c]=4
  if i<t:
   for c in i+l-t+2,r-2+t-i:
    if-1<c<len(g):h[c]=4
 return g
