def p(g):# extend by prefix
 for r in g:
  i=15
  while i>0==r[i-1]:i-=1
  if i:
   s=r[:i];p=1
   while s[p:]!=s[:-p]:p+=1
   r[:]=(s[:p]*(15//p+1))[:15]
 return g
