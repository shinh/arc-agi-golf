# expand each colored cell to a star pattern
p=lambda g:(G:=[[0]*9for _ in g],[G[k//9+i//3-1].__setitem__(k%9+i%3-1,5-4*(i%2))for k in range(81) if sum(g,[])[k] for i in(0,1,2,3,5,6,7,8)])[0]

