R=range(1,12)
#fill
def p(a):
 for i in R:
  for j in R:
   if(g:=a[i-1][j])==(r:=a[i])[j-1]>r[j]:
    for q in a[i:i+(s:=r[j:].index(g))]:q[j:j+s]=[g+s]*s
 return a
