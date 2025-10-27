def p(g):
 e=enumerate
 s={x+y*1j for x,r in e(g)for y,v in e(r)if v};m={*s}
 while s:
  c={s.pop()}
  while(t:={q for q in s for p in c if abs(q-p)<2}):
   c|=t;s-=t
  if len(c)<len(m):m=c
 return[[v and 1+(x+y*1j in m)for y,v in e(r)]for x,r in e(g)]
