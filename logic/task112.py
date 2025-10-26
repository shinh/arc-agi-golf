def p(a):
 w=len(a[0]);s=sum(a,[]);t=s.index(3);r=t//w*2+1;t=t%w*2+1
 for k,v in enumerate(s):
  if v:p=a[r-k//w];p[k%w]=p[t-k%w]=a[k//w][t-k%w]=v
 return a