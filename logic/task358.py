def p(g):# expand patterns horizontally then vertically
	for _ in 0,1:
		for r in g:
			if(S:=[x for x,v in enumerate(r)if v])[1:]:R=r[S[0]:S[-1]+1];break
		r[:]=(R*32)[-S[0]%len(R):][:len(r)];g=[*map(list,zip(*g))]
	return g
