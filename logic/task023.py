def p(g):
 w=len(g[0]);s={i for i,x in enumerate(sum(g,[]))if x>4}
 def f():
  if not s:return g
  n=min(s)
  for e,c in((0,w,2*w),2),((0,1,2),2),((0,1,w,w+1),8):
   if s>={n+o for o in e}:
    for o in e:s.remove(n+o);g[(n+o)//w][(n+o)%w]=c
    if f():return g
    for o in e:s.add(n+o);g[(n+o)//w][(n+o)%w]=5
 return f()
