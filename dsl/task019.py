EIGHT = 8
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
def ineighbors(loc):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def underfill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 bg = mostcolor(grid)
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   if grid_filled[i][j] == bg:
    grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def vconcat(a,b):
 return a + b
def verify_task019(I):
 x0 = hconcat(I, I)
 x1 = vconcat(x0, x0)
 x2 = asindices(x1)
 x3 = mostcolor(I)
 x4 = ofcolor(x1, x3)
 x5 = difference(x2, x4)
 x6 = mapply(ineighbors, x5)
 x7 = underfill(x1, EIGHT, x6)
 return x7
def p(g):
 return [list(r)for r in verify_task019(tuple(tuple(r) for r in g))]