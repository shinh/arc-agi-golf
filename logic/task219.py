def p(b):
 j=len(b);g=len(b[0]);i=0;l=()
 while i<j:
  if 8 in b[i]:
   t=[]
   while 8 in b[i]:
    t+=[(c,i)for c,x in enumerate(b[i])if x>7];i+=1
   t.sort()
   if l:
    z=l[0]
    for e in range(len(t)*2):
     h={(x+t[e>>1][0]-z[0]-(e&1),y+t[e>>1][1]-z[1])for x,y in l};m=set(t[e>>1:])
     if m<=h and min([x for x,y in h-m if x>=0]+[t[-1][0]+1])>t[-1][0]:
      for x,y in h:
       if 0<=x<g and b[y][x]<1:b[y][x]=1
      break
   else:l=t
  else:i+=1
 return b