# row/col propagation
f=lambda g:[*zip(*(map(max,*[s for s in g if max(a*b*(a^b)for a,b in zip(r,s))<1])for r in g))]
p=lambda g:f(f(g))
