def p(a):
 f=sum(a,[]);p=f.index(1);i,j=divmod(p+f.index(1,p+1)>>1,len(a[0]))
 for k in-1,0,1:a[i][j+k]=a[i+k][j]=3
 return a