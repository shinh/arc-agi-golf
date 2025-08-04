FIVE = 5
ONE = 1
THREE = 3
THREE_BY_THREE = (3, 3)
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def color(
 obj
):
 return next(iter(obj))[0]
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
def downscale(
 grid,
 factor
):
 h, w = len(grid), len(grid[0])
 downscaled_grid = tuple()
 for i in range(h):
  downscaled_row = tuple()
  for j in range(w):
   if j % factor == 0:
    downscaled_row = downscaled_row + (grid[i][j],)
  downscaled_grid = downscaled_grid + (downscaled_row, )
 h = len(downscaled_grid)
 downscaled_grid2 = tuple()
 for i in range(h):
  if i % factor == 0:
   downscaled_grid2 = downscaled_grid2 + (downscaled_grid[i],)
 return downscaled_grid2
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
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def last(
 container
):
 return max(enumerate(container))[1]
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
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def width(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
def shift(
 patch,
 directions
):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def verify_task130(I):
 x0 = canvas(ZERO, THREE_BY_THREE)
 x1 = asindices(x0)
 x2 = shape(I)
 x3 = divide(x2, THREE)
 x4 = first(x3)
 x5 = last(x3)
 x6 = interval(ZERO, x4, ONE)
 x7 = interval(ZERO, x5, ONE)
 x8 = product(x6, x7)
 x9 = rbind(multiply, THREE)
 x10 = apply(x9, x8)
 x11 = matcher(first, FIVE)
 x12 = compose(flip, x11)
 x13 = rbind(sfilter, x12)
 x14 = rbind(toobject, I)
 x15 = lbind(shift, x1)
 x16 = chain(x13, x14, x15)
 x17 = compose(color, x16)
 x18 = lbind(shift, x1)
 x19 = fork(recolor, x17, x18)
 x20 = mapply(x19, x10)
 x21 = paint(I, x20)
 x22 = downscale(x21, THREE)
 return x22
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]