def verify_task380(I):
 x0 = rot270(I)
 return x0
def p(g):
 return [list(r)for r in verify_task380(tuple(tuple(r) for r in g))]