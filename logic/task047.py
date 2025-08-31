# draw lines
p=lambda g:[[[c,7,8,2][(7 in(rt:=r+[*t]))+(8 in rt)*2]for c,t in zip(r,zip(*g))]for r in g]
