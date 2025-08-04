def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(
 patch
):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def delta(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 return backdrop(patch) - toindices(patch)
def lbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(
 grid,
 obj
):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def rbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def identity(
 x
):
 return x
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
TWO = 2
def verify_task258(I):
 x0 = leastcolor(I)
 x1 = height(I)
 x2 = vsplit(I, x1)
 x3 = lbind(recolor, TWO)
 x4 = rbind(ofcolor, x0)
 x5 = chain(x3, delta, x4)
 x6 = fork(paint, identity, x5)
 x7 = apply(x6, x2)
 x8 = merge(x7)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]