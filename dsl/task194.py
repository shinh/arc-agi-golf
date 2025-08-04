def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
def vconcat(a,b):
 return a + b
def verify_task194(I):
 x0 = rot90(I)
 x1 = rot180(I)
 x2 = rot270(I)
 x3 = hconcat(I, x0)
 x4 = hconcat(x2, x1)
 x5 = vconcat(x3, x4)
 return x5
def p(g):
 return [list(r)for r in verify_task194(tuple(tuple(r) for r in g))]