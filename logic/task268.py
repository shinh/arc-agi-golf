def p(g,k=0):
 z=zip;E=enumerate
 a=[i for i,x in E(g)if any(x)];b=[i for i,x in E(z(*g))if any(x)];t=a[0];B=a[-1];l=b[0];r=b[-1]
 if 0not in g[t][l:r+1]:return p([*z(*g[::-1])],k+1)
 g=[*map(list,g)]
 for i in range(B):
  s=i<=t;L=l+1+s;g[i][L:r-s]=[4]*(r-s-L)
  if i<t:
   for c in i+l-t+2,r-2+t-i:
    if 0<=c<len(g):g[i][c]=4
 for _ in range(-k%4):g=[*z(*g[::-1])]
 return g