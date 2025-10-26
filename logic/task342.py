def p(g):
 s=sum(g,[]);b=s.index(8);A=[0]*100
 for i,x in enumerate(s):
  if x&7:A[b+(i-b>9)*10+(i%10>b%10)]=x
 return[*zip(*[iter(A)]*10)]