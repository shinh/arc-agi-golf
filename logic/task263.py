def p(g):
 m=-1;B=None
 for y in range(0,len(g),3):
  for x in range(0,len(g[0]),3):
   b=[r[x:x+3]for r in g[y:y+3]]
   s=sum(c>0 for r in b for c in r);c=max(c for r in b for c in r)
   if(s,c)>(m,-1):m=s;B=b
 return B
