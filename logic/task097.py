# zero singles
p=lambda g:[[c*(sum(r[x-(x>0):x+2].count(c)for r in g[y-(y>0):y+2])>1)for x,c in enumerate(r)]for y,r in enumerate(g)]

