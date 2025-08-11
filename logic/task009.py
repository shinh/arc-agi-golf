def p(g,R=range):
 X=[r[:]for r in g]
 n,m=len(g),len(g[0])
 C=g[0][2]
 for i in R(n):
  for j in R(m):
    if g[i][j]==C:
     X[i][j]=C
     g[i][j]=0
    else:X[i][j]=0
 res=[r[:]for r in g]
 for c in R(n):
  pos=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c]
  for i in R(len(pos)):
   for j in R(i+1,len(pos)):
    y1,x1=pos[i]
    y2,x2=pos[j]
    if y1==y2:
     for x in R(min(x1,x2),max(x1,x2)+1):
      res[y1][x]=c
    elif x1==x2:
     for y in R(min(y1,y2),max(y1,y2)+1):
      res[y][x1]=c
 for i in R(n):
  for j in R(m):
    if X[i][j]>0:res[i][j]=C
 return res
