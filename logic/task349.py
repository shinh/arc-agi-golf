def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v>8 and(y<1 or g[y-1][x]-9)and(x<1 or r[x-1]-9):
    a=b=1
    while r[x+a:x+a+1]==[9]:a+=1
    while g[y+b:y+b+1]and g[y+b][x]==9:b+=1
    for R in g[y+b:]:R[x:x+a]=[t or 1 for t in R[x:x+a]]
    q=a>>1
    for R in g[max(y-q,0):y+b+q]:U=max(x-q,0);R[U:x+a+q]=[max(k,3)for k in R[U:x+a+q]]
 return g
