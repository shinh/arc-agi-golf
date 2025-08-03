def p(g):
 d={}
 for r in g:
  for v in r:
   if v:d[v]=d.get(v,0)+1
 m=max(d.values());
 for k in list(d):
  if d[k]==m:del d[k];break
 c=sorted(d,key=d.get,reverse=True)
 return[[c[0]],[c[1]],[c[2]]]
