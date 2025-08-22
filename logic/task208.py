# copy frame
# duplicate rectangular frame to first empty spot
def p(g):
 n=len(g)
 for c in range(1,10):
  P=[(i,j)for i in range(n)for j in range(n)if g[i][j]==c]
  if P:
   r0=min(i for i,j in P);r1=max(i for i,j in P);c0=min(j for i,j in P);c1=max(j for i,j in P);h=r1-r0+1;w=c1-c0+1
   if h>2<w and len(P)==2*(h+w)-4:
    for i in range(n-h+1):
     for j in range(n-w+1):
      if(i,j)!=(r0,c0)and not any(g[i+x][j+y]for x in range(1,h-1)for y in range(1,w-1)):
       for x in range(h):g[i+x][j]=g[i+x][j+w-1]=c
       for y in range(w):g[i][j+y]=g[i+h-1][j+y]=c
       return g
