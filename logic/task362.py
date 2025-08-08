def p(g):
 k=sum(r[-1]==5 for r in g);y=-1
 for r in g:
  y+=1;x=-1
  for v in r:
   x+=1
   if v and v-5:c=v;p=x
  if r.count(c)==10:s=y
 p-=k;s+=k
 o=create(10,10)
 for y in range(10):
  if y==s:o[y]=[c]*10
  else:o[y][p]=c
 return o
