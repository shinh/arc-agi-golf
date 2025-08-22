def p(g):# connect matching digits with straight lines
	d={}
	for y,r in enumerate(g):
		for x,v in enumerate(r):
			if v in d:
				Y,X=d[v]
				while X-x|Y-y:g[Y][X]=v;Y+=Y<y;Y-=Y>y;X+=X<x;X-=X>x
			if v:d[v]=y,x
	return g
