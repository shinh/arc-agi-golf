ONE = 1
THREE = 3
TWO = 2
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
def hfrontier(location):
 return frozenset((location[0], j) for j in range(30))
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def verify_task024(I):
 x0 = ofcolor(I, TWO)
 x1 = ofcolor(I, THREE)
 x2 = ofcolor(I, ONE)
 x3 = mapply(vfrontier, x0)
 x4 = mapply(hfrontier, x1)
 x5 = mapply(hfrontier, x2)
 x6 = fill(I, TWO, x3)
 x7 = fill(x6, THREE, x4)
 x8 = fill(x7, ONE, x5)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]