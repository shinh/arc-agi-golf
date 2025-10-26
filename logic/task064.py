def p(g):#fill
 a=sum(g,[]);c=a.count;s=min(a,key=c);m=min({*a}-{s},key=c)
 for _ in'0'*4:
  for r in g:
   try:i,j=r.index(s),r.index(m);r[i+1:j]=[s]*(j-i-1)
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g