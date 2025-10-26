def p(g):
 f=sum(g,[])
 t=[i for i in range(100)if f[i]%8];a=t[0]
 while 8 in f:
  j=f.index(8)
  for i in t:f[j+i-a]=f[i]
 for i in t:f[i]=0
 return[*zip(*[iter(f)]*10)]