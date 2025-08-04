ONE = 1
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(
 a,
 b
):
 return (a, b)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def contained(
 value,
 container
):
 return value in container
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
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def hperiod(
 obj
):
 normalized = normalize(obj)
 w = width(normalized)
 for p in range(1, w):
  offsetted = shift(normalized, (0, -p))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
  if pruned.issubset(normalized):
   return p
 return w
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def maximum(
 container
):
 return max(container, default=0)
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def shape(
 piece
):
 return (height(piece), width(piece))
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task394(I):
 x0 = lbind(contained, ZERO)
 x1 = compose(flip, x0)
 x2 = sfilter(I, x1)
 x3 = dmirror(I)
 x4 = lbind(contained, ZERO)
 x5 = compose(flip, x4)
 x6 = sfilter(x3, x5)
 x7 = compose(hperiod, asobject)
 x8 = height(x2)
 x9 = vsplit(x2, x8)
 x10 = apply(x7, x9)
 x11 = maximum(x10)
 x12 = compose(hperiod, asobject)
 x13 = height(x6)
 x14 = vsplit(x6, x13)
 x15 = apply(x12, x14)
 x16 = maximum(x15)
 x17 = ofcolor(I, ZERO)
 x18 = asobject(I)
 x19 = matcher(first, ZERO)
 x20 = compose(flip, x19)
 x21 = sfilter(x18, x20)
 x22 = lbind(shift, x21)
 x23 = height(I)
 x24 = divide(x23, x16)
 x25 = increment(x24)
 x26 = width(I)
 x27 = divide(x26, x11)
 x28 = increment(x27)
 x29 = invert(x25)
 x30 = increment(x25)
 x31 = interval(x29, x30, ONE)
 x32 = invert(x28)
 x33 = increment(x28)
 x34 = interval(x32, x33, ONE)
 x35 = product(x31, x34)
 x36 = astuple(x16, x11)
 x37 = lbind(multiply, x36)
 x38 = apply(x37, x35)
 x39 = mapply(x22, x38)
 x40 = paint(I, x39)
 x41 = subgrid(x17, x40)
 return x41
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]