def p(a):
 w=len(a[0]);b=sum(a,[]);s=b.index(3);t=s%w*2+1;s=s//w*2+1
 for k,v in enumerate(b):
  if v%3:i=k//w;j=k%w;a[s-i][j]=a[i][t-j]=a[s-i][t-j]=2
 return a