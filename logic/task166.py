# fill rectangle enclosed by 8s with 2
# Far from the best. hmm.
p=lambda g:[[t[0]or(8in r)*any(t)*2 for t in zip(r,*g)]for r in g]
