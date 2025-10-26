# Golf.
# Task390.
# rotate chunk
def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g))][::-1]):
   if{2,5}<={*r}:a=r[4]==2;r[a:a+7]=0,0,*r[a+2:a+5],r[a+1],r[a]
 return g
