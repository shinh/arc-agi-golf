def p(g):
 # map quadrants
 s=sum(g,[]);b=s.index(8);A=[0]*100
 for i,x in enumerate(s):A[b+(i-b>9)*10+(i%10>b%10)]+=x&7and x
 return[*zip(*[iter(A)]*10)]