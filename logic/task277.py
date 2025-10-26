def p(g):
 s={x+y*1j for x,r in enumerate(g)for y,v in enumerate(r)if v};m=s|{0}
 while s:
  c={s.pop()}
  while(t:={q for q in s for p in c if 0<abs(q-p)<2}):
   c|=t;s-=t
  if len(c)<len(m):m=c
 return[[v and 1+(x+y*1j in m)for y,v in enumerate(r)]for x,r in enumerate(g)]
