def p(g):
 # repeat biggest 3x3 block indicated by hints
 e=max(g[0]);R=range(19);T=0,1,2;B=max(([(y+i,x+j)for i in T for j in T if g[y+i][x+j]^e]for y in R for x in R),key=len)
 for s in(-4,0,4):
  for t in(-4,0,4):
   if(s|t)*any(0<=(u:=y+s)<21>(v:=x+t)>=0 and (c:=g[u][v])^e for y,x in B):
    for k in range(1,6):
     for y,x in B:
      if 0<=(u:=y+s*k)<21>(v:=x+t*k)>=0:g[u][v]=c
 return g
