def p(g):
 c=[]
 for r in g:
  for v in r:
   if v and v not in c:c.append(v)
 a,b=c[0],c[-1]
 h=len(g);w=len(g[0])
 for i in range(1,h-1):
  for j in range(1,w-1):
   if g[i][j]==b and all(g[i+di][j+dj]==a for di in(-1,0,1) for dj in(-1,0,1) if di or dj):
    return[[b]]
 return[[a]]
