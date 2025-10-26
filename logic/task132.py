def p(g):
 w,b=len(g[0]),sum(g,[])
 for v in{*b}-{0}:
  i=b.index;a=i(v);d=i(v,a+1);y,l=sorted((a%w,d%w))
  for r in g[a//w:d//w+1]:r[y:l+1]=[v]*(l-y+1)
 return g