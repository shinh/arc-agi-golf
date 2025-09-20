def p(g):# extend by prefix
 for r in g:
  while r[-1]<1<sum(r):r.pop()
  p=1
  while r[p:]!=r[:-p]:p+=1
  r[:]=(r[:p]*15)[:15]
 return g
