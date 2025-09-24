# Golf.
# Task390.
# rotate left chunk right & clear
def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{2,5}<={*r}:a=r.index(2)-3;r[a+5:a+7]=r[a+1],r[a];r[a:a+2]=0,0
 return g
