def p(g):
 o=[]
 for r in g:
  m={}
  nr=[]
  for i in range(len(r)):
   c=r[i]
   if c:
    m[g[1][i]]=c
   elif m:
    c=m[g[1][i]]
   nr.append(c)
  o.append(nr)
 return o
