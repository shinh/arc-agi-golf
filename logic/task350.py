def p(g):
 # connect 1s
 def f(s):
  for r in s:
   l=-1
   for x,v in enumerate(r):
    if v==1:
     if~l:r[l+1:x]=[8]*(x-l-1)
     l=x
 f(g)
 t=[*map(list,zip(*g))]
 f(t)
 g[:]=map(list,zip(*t))
 return g

