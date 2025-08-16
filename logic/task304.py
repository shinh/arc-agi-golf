# replicate g in each cell matching the most common color
p=lambda g,r=range(9):[[g[i%3][j%3]*(max(f:=sum(g,[]),key=f.count)==g[i//3][j//3])for j in r]for i in r]
