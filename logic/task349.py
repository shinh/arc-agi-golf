def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v-9 or y and g[y-1][x]==9 or x and r[x-1]==9:continue
   a=b=1
   while x+a<len(r)and r[x+a]==9:a+=1
   while y+b<len(g)and g[y+b][x]==9:b+=1
   for R in g[y+b:]:R[x:x+a]=[t or 1 for t in R[x:x+a]]
   q=a//2
   s=max(0,y-q);t=max(0,x-q)
   for R in g[s:y+b+q]:R[t:x+a+q]=[max(k,3)for k in R[t:x+a+q]]
 return g
