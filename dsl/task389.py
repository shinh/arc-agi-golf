FIVE = 5
ZERO = 0
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def remove(value,container):
 return type(container)(e for e in container if e != value)
def verify_task389(I):
 x0 = palette(I)
 x1 = remove(FIVE, x0)
 x2 = first(x1)
 x3 = ofcolor(I, x2)
 x4 = fill(I, ZERO, x3)
 x5 = ofcolor(I, FIVE)
 x6 = fill(x4, x2, x5)
 return x6
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]