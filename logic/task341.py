def p(l,e=enumerate):
 def f():
  a=[i for i,r in e(l)if len({*r})>2]
  for i in a[1:-1]:
   r=l[i]=[*l[i]];s=set()
   for j,v in e(r):
    v and s.add(v);r[j]=v or 8*(len(s)==1)
 f();l=[*zip(*l[::-1])];f();return[*zip(*l)][::-1]