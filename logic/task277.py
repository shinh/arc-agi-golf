def p(g):
 j=1j;s={x+j*y for x,r in enumerate(g)for y,v in enumerate(r)if v};b=0
 while s:
  c={s.pop()}
  while(t:={p+a+b*j for p in c for a in(-1,0,1)for b in(-1,0,1)if a|b}&s):
   c|=t;s-=t
  b=b and min(c,b,key=len)or c
 return[[v and 1+(x+j*y in b)for y,v in enumerate(r)]for x,r in enumerate(g)]