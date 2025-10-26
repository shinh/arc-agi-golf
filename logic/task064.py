def p(g):#fill
 a=sum(g,[]);c=a.count;s=min(a,key=c);m=min({*a}-{s},key=c)
 for _ in'0'*4:
  for r in g:
   try:i,j=map(r.index,(s,m));r[i+1:j]=[s]*~(i-j)
   except:0
  g=[*map(list,zip(*g))][::-1]
 return g
