def p(a):
 s={(i,j)for i,r in enumerate(a)for j,v in enumerate(r)if v}
 for i,j in s:
  if{(i+1,j),(i-1,j),(i,j+1),(i,j-1)}&s:
   for t in a[i and i-1:i+2]:
    k=j and j-1;t[k:j+2]=[x or 3 for x in t[k:j+2]]
 return a