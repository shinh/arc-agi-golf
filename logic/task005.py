def p(g):
 # repeat biggest 3x3 block indicated by hints
 e=max(g[0]);R=range(19);B=max(([(y+i,x+j)for i in(0,1,2)for j in(0,1,2)if g[y+i][x+j]-e]for y in R for x in R),key=len)
 for s in -4,0,4:
  for t in -4,0,4:
   if s|t:
    for y,x in B:
     if-1<(u:=y+s)<21 and -1<(v:=x+t)<21 and (c:=g[u][v])-e:break
    else:continue
    for k in 1,2,3,4,5:
     for y,x in B:
      if-1<(u:=y+s*k)<21 and -1<(v:=x+t*k)<21:g[u][v]=c
 return g
