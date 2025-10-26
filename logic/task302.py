def p(a):
 R=range(1,12)
 for i in R:
  r=a[i]
  for j in R:
   if r[j]<1<(g:=a[i-1][j])==r[j-1]:
    s=r[j:].index(g)
    for q in a[i:i+s]:q[j:j+s]=[g+s]*s
 return a