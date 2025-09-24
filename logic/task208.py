# copy frame
# duplicate rectangular frame to first empty spot
def p(g):
 n=len(g);R=range
 for c in R(1,10):
  a=b=n;d=e=-1;m=0
  for y in R(n):
   for x in R(n):
    if g[y][x]==c:
     m+=1
     a=min(a,y);d=max(d,y);b=min(b,x);e=max(e,x)
  h=d-a+1;w=e-b+1
  if h>2<w and m+4==2*(h+w):
   for y in R(n-h+1):
    for x in R(n-w+1):
     if(y,x)!=(a,b)and not any(g[y+u][x+v]for u in R(1,h-1)for v in R(1,w-1)):
      for u in R(h):g[y+u][x]=g[y+u][x+w-1]=c
      for v in R(w):g[y][x+v]=g[y+h-1][x+v]=c
      return g
