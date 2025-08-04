def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def verify_task380(I):
 x0 = rot270(I)
 return x0
def p(g):
 return [list(r)for r in verify_task380(tuple(tuple(r) for r in g))]