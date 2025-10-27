def p(g):
	g=sum(g,[]);i=g.index
	for v in{*g}-{0}:a=i(v);d=i(v,a+1)-a;s=9+(d%9>0)*2;g[a:a+d+s:s]=[v]*-~(d//s)
	return[*zip(*[iter(g)]*10)]
