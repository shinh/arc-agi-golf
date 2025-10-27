def p(g):
 w=len(g[0]);s={i for i,x in enumerate(sum(g,[]))if x>4}
 def f():
  nonlocal s
  if not s:return g
  n=min(s)
  for *e,c in((0,w,2*w,2),(0,1,2,2),(0,1,w,w+1,8)):
   if (t:={n+o for o in e})<=s:
    s^=t
    for i in t:g[i//w][i%w]=c
    if f():return g
    s^=t
    for i in t:g[i//w][i%w]=5
 return f()
