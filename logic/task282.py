# expand each colored cell to a star pattern
p=lambda g:(G:=[[0]*9for _ in g],[G[k//9+a].__setitem__(k%9+b,(1,5)[a*b])for k in range(81)for a in(-1,0,1)for b in(-1,0,1)if sum(g,[])[k]*(a|b)])[0]

