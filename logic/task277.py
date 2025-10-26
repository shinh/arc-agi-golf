def p(g):
 R=-1,0,1;L=[];s={x+y*1j for x,r in enumerate(g)for y,v in enumerate(r)if v}
 while s:
  c={s.pop()}
  while(t:={p+a+b*1j for p in c for a in R for b in R if a|b}&s):
   c|=t;s-=t
  L+=c,
 return[[v and 1+(x+y*1j in min(L,key=len))for y,v in enumerate(r)]for x,r in enumerate(g)]
