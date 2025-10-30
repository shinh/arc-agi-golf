def p(g):#f
 a=sum(g,[]);s,m,*_=sorted(sorted({*a}),key=a.count)
 for _ in'0'*4:
  for r in g:
   try:i,j=map(r.index,(s,m));r[i:j]=[s]*(j-i)
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g
