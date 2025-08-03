def p(g):
 r=g[0];w=len(r);c=r[0];l=0
 while l<w and r[l]==c:l+=1
 o=[r]
 for i in range(w//2-1):
  r=r.copy();r[l+i]=c;o+= [r]
 return o
