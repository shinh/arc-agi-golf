def p(g):
 a=sum(g,[]);s=min(a,key=a.count);m=({*a}-{s,max(a,key=a.count)}).pop()
 for _ in'1111':
  for r in g:
   try:i=r.index(s);j=r.index(m);r[i+1:j]=[s]*(j-i-1)
   except:0
  g=[[*x]for x in zip(*g[::-1])]
 return g