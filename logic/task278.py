def p(a):
 for i,j in(s:={(i,j)for i,r in enumerate(a)for j,v in enumerate(r)if v}):
  if(i+1,j)in s or(i-1,j)in s or(i,j+1)in s or(i,j-1)in s:
   for t in a[i-(i>0):i+2]:t[j-(j>0):j+2]=[x or 3 for x in t[j-(j>0):j+2]]
 return a
