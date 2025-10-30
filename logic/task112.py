def p(a):
 w=len(a[0]);s=sum(a,[]);t=s.index(3);r=t//w*2+1;t=t%w*2+1;k=0
 for v in s:
  if v:b=a[r-k//w];b[k%w]=b[d:=t-k%w]=a[k//w][d]=v
  k+=1
 return a
