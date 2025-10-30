def p(a):
 for i,j in(s:={(i,j)for i,r in enumerate(a)for j,v in enumerate(r)if v}):
  if s&{(i+1,j),(i,j+1),(i-1,j),(i,j-1)}:
   for t in a[i-(i>0):i+2]:t[j-(j>0):j+2]=[x or 3 for x in t[j-(j>0):j+2]]
 return a
