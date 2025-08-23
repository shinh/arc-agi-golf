# prefer left then mid else keep
p=lambda g:[[max(r[c::5],key=bool)for c in(0,1,2,3)]for r in g]

