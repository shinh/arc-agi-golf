# copy frame
def p(g):
 n=len(g);o=[r[:]for r in g]
 for c in range(1,10):
  P=[(i,j)for i in range(n)for j in range(n)if g[i][j]==c]
  if P:
   r0=min(i for i,j in P);r1=max(i for i,j in P);c0=min(j for i,j in P);c1=max(j for i,j in P)
   h=r1-r0+1;w=c1-c0+1
   if h>2<w and len(P)==2*h+2*w-4 and all(i in(r0,r1)or j in(c0,c1)for i,j in P):
    for i in range(n-h+1):
     for j in range(n-w+1):
      if(i,j)!=(r0,c0)and all(g[i+x][j+y]<1 for x in range(h)for y in range(w) if x*y*(x-h+1)*(y-w+1)):
       for x in range(h):
        for y in range(w):
         if x*y*(x-h+1)*(y-w+1)==0:o[i+x][j+y]=c
       return o
