def p(g):#stripe
 r=g[9];v=sum(r);j=r.index(v);t=9
 while j<10:
  for r in g:r[j]=v
  if j-9:t^=9;g[t][j+1]=5
  j+=2
 return g
