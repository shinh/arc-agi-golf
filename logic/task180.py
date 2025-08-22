# merge quadrants taking colors in priority order
p=lambda g:[[max(z,key=bool)for z in zip(r[4:],s,s[4:],r)]for r,s in zip(g,g[4:])]
