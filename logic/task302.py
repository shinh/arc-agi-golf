R=range(1,12)
#fill
def p(a):
 for i in R:
  for j in R:
   if a[i-1][j]==(r:=a[i])[j-1]==5>r[j]:
    for q in a[i:i+(s:=r[j:].index(5))]:q[j:j+s]=[5+s]*s
 return a
