def p(l,E=enumerate):
 # row/col 8 bridge
 def g():
  for i in [i for i,r in E(l)if len({*r})>2][1:-1]:
   r=l[i]=[*l[i]];s=set()
   for j,v in E(r):
    v and s.add(v);r[j]=v or(len(s)==1)*8
 g();l=[*zip(*l[::-1])];g();return[*zip(*l)][::-1]
