def p(g):#stripe
	j=g[9].index(v:=sum(g[9]));t=9
	while j<10:
		for r in g:r[j]=v
		if j<9:g[t:=t^9][j+1]=5
		j+=2
	return g
