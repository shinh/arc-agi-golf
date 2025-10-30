def p(g):
 m=max
 for y,r in enumerate(g):
   for x,v in enumerate(r):
    if v>8>=m(x and r[x-1],y and g[y-1][x]):
     a=b=1
     while r[x+a:x+a+1]>[8]:a+=1
     while g[y+b:y+b+1]and g[y+b][x]>8:b+=1
     for R in g[y+b:]:R[x:x+a]=[t or 1 for t in R[x:x+a]]
     q=a>>1
     for R in g[m(y-q,0):y+b+q]:U=m(x-q,0);R[U:x+a+q]=[m(k,3)for k in R[U:x+a+q]]
 return g
