def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
def verify_task249(I):
 x0 = hconcat(I, I)
 return x0
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]