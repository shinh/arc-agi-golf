def p(g):
	#crop blank/dupe
	return*(f:=lambda g:zip(*filter(sum,{}.fromkeys(map(tuple,g)))))(f(g)),