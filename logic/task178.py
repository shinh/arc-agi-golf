def f(g):
 h=p=()
 for r in g:h+=(r,)*(r!=p);p=r
 return h
p=lambda g:f(zip(*f(zip(*g))))# dedup cols then rows
