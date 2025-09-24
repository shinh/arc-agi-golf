def p(g):# fill inside 5 square
 for y in range(1,11):
  r=g[y]
  for x in range(1,11):
   if g[y-1][x]==r[x-1]>r[x]:
    n=1
    while r[x+n]<1:n+=1
    for q in g[y:y+n]:q[x:x+n]=[n+5]*n
 return g
