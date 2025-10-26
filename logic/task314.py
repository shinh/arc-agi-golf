def p(g):#fill
	for i in 0,1,3,4,6,7:
		for j in 0,1:
			if(a:=g[i][j])==g[i][j+6]!=1:g[i][j+3]=a
			if(b:=g[j][i])==g[j+6][i]!=1:g[j+3][i]=b
	return g
