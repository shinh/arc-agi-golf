def p(g):
 z=zip;E=enumerate
 g=[*map(list,g)]
 t,*_,B=[i for i,x in E(g)if any(x)];l,*_,r=[i for i,x in E(z(*g))if any(x)]
 if all(g[t][l:r+1]):return [*z(*p([*z(*g[::-1])]))][::-1]
 for i in range(B):
  s=i<=t;L=l+1+s;h=g[i];h[L:r-s]=[4]*(r-s-L)
  if i<t:
   for c in i+l-t+2,r-2+t-i:
    if-1<c<len(g):h[c]=4
 return g
