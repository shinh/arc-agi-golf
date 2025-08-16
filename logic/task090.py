def p(g):
 # fill largest empty rectangles with 6
 h=len(g);w=len(g[0]);r=range;m=0;R=[]
 for a in r(h):
  for b in r(w):
   for c in r(a+2,h+1):
    for d in r(b+2,w+1):
     if not any(g[y][x]for y in r(a,c)for x in r(b,d)):
      if m<(n:=(c-a)*(d-b)):m=n;R=[(a,b,c,d)]
      elif m==n:R+=(a,b,c,d),
 for a,b,c,d in R:
  for y in r(a,c):g[y][b:d]=[6]*(d-b)
 return g

