def p(g):
 for k,a in enumerate(t:=sum(g,[])):
  if 0<a<3:
   for d in(7*a-6,a+8):t[k+d]=t[k-d]=10-3*a
 return[*zip(*[iter(t)]*9)]