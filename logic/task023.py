def p(g):
 w=len(g[0]);t=sum(g,[]);s={i for i,x in enumerate(t)if x>4}
 def f():
  if not s:return 1
  n=min(s)
  for e,c in((0,w,2*w),2),((0,1,2),2),((0,1,w,w+1),8):
   if all(n+o in s for o in e):
    for o in e:s.remove(n+o);g[(n+o)//w][(n+o)%w]=c
    if f():return 1
    for o in e:s.add(n+o);g[(n+o)//w][(n+o)%w]=5
 f();return g