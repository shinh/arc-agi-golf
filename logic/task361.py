def p(g):
 h=w=10
 for k in range(min(h,w),0,-1):
  for i in range(h-k+1):
   for j in range(w-k+1):
    if all(g[i+y][j+x] for y in range(k) for x in range(k)):
     c=i+(k-1)/2;d=j+(k-1)/2;o=[r[:] for r in g]
     for y,r in enumerate(g):
      for x,v in enumerate(r):
       if v and (y<i or y>=i+k or x<j or x>=j+k):
        a=y-c;b=x-d
        for a,b in(-b,a),(-a,-b),(b,-a):
         y2=round(c+a);x2=round(d+b)
         if 0<=y2<h and 0<=x2<w:o[y2][x2]=v
     return o
 return g
