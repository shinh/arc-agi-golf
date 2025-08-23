# cycle the 3 diagonal colors
p=lambda g:(t:=(g[0][0],g[1][1],g[2][2]))and[[t[t.index(v)-1]for v in r]for r in g]

