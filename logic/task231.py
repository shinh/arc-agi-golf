def p(g):
 o=[]
 for r in g:
  w=len(r)
  for p in range(1,w+1):
   if all(r[i]==r[i-p]for i in range(p,w)):break
  s=w%p
  o.append(r+[r[i%p]for i in range(s,s+w)])
 return o
