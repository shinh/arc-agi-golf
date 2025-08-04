SIX = 6
THREE = 3
ZERO = 0
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def divide(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def equality(
 a,
 b
):
 return a == b
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
def fill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def identity(
 x
):
 return x
def last(
 container
):
 return max(enumerate(container))[1]
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def verify_task292(I):
 x0 = asobject(I)
 x1 = matcher(first, ZERO)
 x2 = compose(flip, x1)
 x3 = sfilter(x0, x2)
 x4 = rbind(multiply, THREE)
 x5 = rbind(divide, THREE)
 x6 = compose(x4, x5)
 x7 = fork(equality, identity, x6)
 x8 = toindices(x3)
 x9 = compose(x7, last)
 x10 = sfilter(x8, x9)
 x11 = fill(I, SIX, x10)
 return x11
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]