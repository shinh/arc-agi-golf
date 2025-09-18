def p(g):#%3
	for r in g[1:]:
		if r[9]:r[:9]=[v%3for v in g[0][:9]]
	return g