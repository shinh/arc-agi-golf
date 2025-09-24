# Not bad, but not golfed yet.
# 120
def p(f):
	for n in sum(f,[]):
		for r in (i:=f)*8:i=[*zip(*i[(n in i[-1])-2::-1])]
		if[i[::-1]for i in i]==i:return i
