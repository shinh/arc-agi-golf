def p(g):#crop 3x3 around 8; center=2nd max
	s=sum(g,[]);g=[s[s.index(8)+o:][:3]for o in(-14,-1,12)];g[1][1]=sorted(sum(g,[]))[7];return g
