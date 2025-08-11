def p(g):
 n=sum(g,[]).count(5)
 o=[]
 for y in range(len(g)):
  nr=[]
  for x in range(len(g[0])):
   c=(g[y-n]*2)[x+n]
   if c%5:
    nr.append(c)
   else:
    nr.append(0)
  o.append(nr)
 return o
