def p(g):
 d={}
 for r in g:
  for v in r:
   if v:d[v]=d.get(v,0)+1
 c=sorted(d,key=d.get,reverse=True)
 return[[c[0]],[c[1]],[c[2]]]
