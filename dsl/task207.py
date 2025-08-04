def astuple(a,b):
 return (a, b)
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def combine(a,b):
 return type(a)((*a, *b))
def leastcommon(container):
 return min(set(container), key=container.count)
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
def verify_task207(I):
 x0 = lefthalf(I)
 x1 = righthalf(I)
 x2 = tophalf(x0)
 x3 = tophalf(x1)
 x4 = bottomhalf(x0)
 x5 = bottomhalf(x1)
 x6 = astuple(x2, x3)
 x7 = astuple(x4, x5)
 x8 = combine(x6, x7)
 x9 = leastcommon(x8)
 return x9
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]