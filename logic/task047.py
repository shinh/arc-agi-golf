# draw lines
p=lambda g:[[[c,7,8,2][(7 in t+r)+(8 in t+r)*2]for c,*t in zip(r,*g)]for r in g]
