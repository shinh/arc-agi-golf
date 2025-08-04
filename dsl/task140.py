def rot180(grid):
 return tuple(tuple(row[::-1]) for row in grid[::-1])
def verify_task140(I):
 x0 = rot180(I)
 return x0
def p(g):
 return [list(r)for r in verify_task140(tuple(tuple(r) for r in g))]