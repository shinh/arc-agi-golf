def p(b):
 g=len(b[0]);s=[];t=[]
 for i,r in enumerate(b):
  if 8 in r:t+=[(c,i)for c,x in enumerate(r)if x>7]
  elif t:s+=sorted(t),;t=[]
 if t:s+=sorted(t),
 l=s[0];z=l[0]
 for t in s[1:]:
  for e in range(len(t)*2):
   a=t[e>>1];h={(x+a[0]-z[0]-(e&1),y+a[1]-z[1])for x,y in l};m=set(t[e>>1:]);q=t[-1][0]
   if m<=h and all(x>q for x,y in h-m if x>=0):
    for x,y in h:
     if 0<=x<g and b[y][x]<1:b[y][x]=1
    break
 return b
