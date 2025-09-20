def p(g):
	#use 1st row/col diag
	for y in range(len(g)):
		for x in range(1,y+1,2):
			if g[0][y-x]:g[x][y]=4
			if g[y-x][0]:g[y][x]=4
	return g
