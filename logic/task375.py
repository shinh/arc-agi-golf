def p(a,i=0):
 for r in a:r[i]=r[~i]=0;i+=1
 return a