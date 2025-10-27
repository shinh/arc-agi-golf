def p(l,E=enumerate):# row/col 8 bridge
 def g():
  for i in [i for i,r in E(l)if len({*r})>2][1:-1]:
   r=l[i]=[*l[i]];t=[j for j,v in E(r)if v];r[t[0]:t[-1]]=[v or 8 for v in r[t[0]:t[-1]]]
 g();l=[*zip(*l[::-1])];g();return[*zip(*l)][::-1]
