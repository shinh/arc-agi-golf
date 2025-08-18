# fill rectangle enclosed by 8s with 2
# 65B. Very close to the known best (63B)
p=lambda g:[[t[0]or(8in r)*any(t)*2 for t in zip(r,*g)]for r in g]
