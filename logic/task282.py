# expand each colored cell to a star pattern
p=lambda g,R=range(1,8):(G:=[[0]*9for _ in g],[G[i+a].__setitem__(j+b,(1,5)[a*b])for i in R for j in R for a in(-1,0,1)for b in(-1,0,1)if g[i][j]*(a|b)])[0]

