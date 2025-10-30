def p(b):
 # reuse base 8 shape to paint 1s
 g=len(b[0]);s=[];t=[]
 for i,r in enumerate(b+[[]]):
  if 8 in r:t+=[(c,i)for c,x in enumerate(r)if x>7]
  elif t:s+=sorted(t),;t=[]
 a=s[0];u,v=a[0]
 for t in s[1:]:
  for e in range(len(t)*2):
   j=e>>1
   q={(x+t[j][0]-u-(e&1),y+t[j][1]-v)for x,y in a}
   if {*t[j:]}<=q:
    for x,y in q:
     if g>x>=0<=y<len(b):b[y][x]=b[y][x]or 1
    break
 return b
