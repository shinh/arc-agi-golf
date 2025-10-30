def p(b):
 g=len(b[0]);s=[];t=[]
 for i,r in enumerate(b+[[]]):
  if 8 in r:t+=[(c,i)for c,x in enumerate(r)if x>7]
  elif t:s+=sorted(t),;t=[]
 u,v=s[0][0]
 for t in s[1:]:
  for e in range(len(t)*2):
   j=e>>1
   if {*t[j:]}<={(x+t[j][0]-u-e%2,y+t[j][1]-v)for x,y in s[0]}:
    for x,y in{(x+t[j][0]-u-e%2,y+t[j][1]-v)for x,y in s[0]}:
     if g>x>=0<=y<len(b)and b[y][x]==0:b[y][x]=1
    break
 return b