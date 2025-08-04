def verify_task087(I):
 x0 = rot180(I)
 return x0
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]