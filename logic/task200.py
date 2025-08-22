def p(g):#stripe
 j,v=next((k%10,v)for k,v in enumerate(sum(g,[]))if v);t=0
 for j in range(j,10,2):
  for r in g:r[j]=v
  if j-9:g[t][j+1]=5;t^=9
 return g

