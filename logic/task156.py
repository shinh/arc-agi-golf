def p(g):
 d=t=0
 for i in range(1,9):
  r=g[i];t^=max(r)<1
  for j in range(1,9):
   if r[j-1]*r[j+1]*g[i-1][j]*g[i+1][j]:
    r[j]=1+t;d+=1-2*t
 return(eval(str(g).translate({49:50,50:49})),g)[d<1]

