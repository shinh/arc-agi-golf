def p(g):
 R=range(1,9)
 d=t=0
 for i in R:
  t^=1>max(r:=g[i])
  for j in R:
   if r[j-1]*r[j+1]*g[i-1][j]*g[i+1][j]:
    d+=1-2*t;r[j]=t+1
 return[g,eval(str(g).translate({49:50,50:49}))][d>0]

