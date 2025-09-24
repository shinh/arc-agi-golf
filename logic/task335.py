def p(g):
	i=sum(g,[]).index;C,A,D,B=divmod(i(8),w:=len(g[0]))+divmod(i(2),w)
	# link 8 to 2 by 4s
	while C-D:C+=D>C or-1;g[C][A]=4
	while A-B:g[D][A]=4;A+=B>A or-1
	return g
