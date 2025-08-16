def p(g):
 # collect empty rectangles and paint the largest with 6
 h=len(g);w=len(g[0]);r=range
 R=[(a,b,c,d)for a in r(h)for b in r(w)for c in r(a+2,h+1)for d in r(b+2,w+1)
    if not any(g[y][x]for y in r(a,c)for x in r(b,d))]
 m=max((c-a)*(d-b)for a,b,c,d in R)
 for a,b,c,d in R:
  if m==(c-a)*(d-b):
   for y in r(a,c):g[y][b:d]=[6]*(d-b)
 return g

