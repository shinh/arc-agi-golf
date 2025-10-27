h=lambda g:[[c or(8in r[:i])*(8in r[i+1:])*3for i,c in enumerate(r)]for r in g]
p=lambda g:h(zip(*h(zip(*g))))
