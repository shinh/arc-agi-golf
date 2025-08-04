def p(g):
 d={5:[],8:[]}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v in d:d[v].append((i,j))
 f=lambda p:(min(i for i,_ in p),max(i for i,_ in p),min(j for _,j in p),max(j for _,j in p))
 a=f(d[5]);b=f(d[8])
 h=a[1]-a[0]+1;w=a[3]-a[2]+1
 h8=b[1]-b[0]+1;w8=b[3]-b[2]+1
 t=all(g[i][a[2]]==5 and g[i][a[3]]==5 for i in range(a[0],a[1]+1))
 n=(h-h8-1) if t else (w-w8-1)
 r=[8]*n+[0]*(9-n)
 return[r[:3],r[3:6][::-1],r[6:9]]
