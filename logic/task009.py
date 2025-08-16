def p(g,R=range,E=enumerate):
 # connect same-colored dots
 C=g[0][2]
 o=[[0]*len(g[0])for _ in g]
 for y,r in E(g):
  for x,v in E(r):
   if v==C:o[y][x]=v
   elif v:
    for X in R(x+1,len(r)):
     if r[X]==v:o[y][x:X+1]=[v]*(X+1-x);break
    for Y in R(y+1,len(g)):
     if g[Y][x]==v:
      for i in R(y,Y+1):o[i][x]=v
      break
 return o
