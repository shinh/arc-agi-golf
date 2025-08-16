def f(g):
    h=[];p=h
    for r in g:h+=[[*r]]*(r!=p);p=r
    return h
# dedup cols then rows
p=lambda g:f(zip(*f(zip(*g))))
