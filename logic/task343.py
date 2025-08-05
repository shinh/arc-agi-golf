def p(g):
 n=15;o=[]
 for r in g:
  i=n
  while i and not r[i-1]:i-=1
  if not i:o.append(r[:]);continue
  for p in range(1,i+1):
   if all(r[k]==r[k%p]for k in range(i)):break
  a=r[:p]
  o.append((a*(n//p+1))[:n])
 return o
