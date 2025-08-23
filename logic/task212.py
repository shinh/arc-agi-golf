# extend lines
p=lambda g:(r:=g.index([5]*10),[row.__setitem__(x,v)for y in range(10)for x,v in enumerate(g[y])if 0<v<3 for row in (g[:y+1],g[y:],g[y:r],g[r+1:y+1])[(v&2)|(y>r)]],g)[2]
