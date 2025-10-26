def p(g):
 m=()
 for y in range(12):
  for x in range(12):
   B=[r[x:x+3]for r in g[y:y+3]];t=sum(B,[]);c=max(t)
   if c and sum(t)==c*(k:=t.count(c))and sum(r[x and x-1:x+4].count(c)for r in g[y and y-1:y+4])==k:m+=B,
 return max(m,key=m.count)