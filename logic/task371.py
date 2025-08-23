def p(g,E=enumerate):
 y,x=(sum(k)//2for k in zip(*((i,j)for i,r in E(g)for j,v in E(r)if v)))
 for i in-1,0,1:g[y+i][x]=g[y][x+i]=3
 return g#place cross at midpoint
