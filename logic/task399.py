def p(g):
 o=create(3,3);k=0
 for r,s in zip(g,g[1:]):
  for a,b,c,d in zip(r,r[1:],s,s[1:]):
   if a+b+c+d==8:o[k*2//3][k*2%3]=1;k+=1
 return o
