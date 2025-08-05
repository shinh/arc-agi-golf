def p(g):
 h=len(g);w=len(g[0]);C=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]<1:
    q=[(y,x)];g[y][x]=2;c=[]
    for i,j in q:
     c+=[(i,j)]
     for a,b in(1,0),(-1,0),(0,1),(0,-1):
      A=i+a;B=j+b
      if 0<=A<h and 0<=B<w and g[A][B]<1:
       g[A][B]=2;q+=[(A,B)]
    C+=[c]
 m=max(len(c)for c in C);n=min(len(c)for c in C)
 for c in C:
  v=1 if len(c)==m else 8 if len(c)==n else 0
  for y,x in c:g[y][x]=v
 return g
