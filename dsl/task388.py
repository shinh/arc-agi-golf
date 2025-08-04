EIGHT = 8
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
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
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def verify_task388(I):
 x0 = fgpartition(I)
 x1 = mapply(toindices, x0)
 x2 = mapply(vfrontier, x1)
 x3 = underfill(I, EIGHT, x2)
 x4 = hconcat(x3, x3)
 x5 = vconcat(x4, x4)
 return x5
def p(g):
 return [list(r)for r in verify_task388(tuple(tuple(r) for r in g))]