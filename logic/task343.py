def p(g):# extend by prefix
 for r in g:
  i=15
  while i>0==r[i-1]:i-=1;p=1
  while r[p:i]!=r[:i-p]:p+=1
  r[:]=(r[:p]*15)[:15]
 return g
