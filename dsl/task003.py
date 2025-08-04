def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def toivec(
 i
):
 return (i, 0)
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
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
ZERO = 0
def add(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def astuple(
 a,
 b
):
 return (a, b)
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def vperiod(
 obj
):
 normalized = normalize(obj)
 h = height(normalized)
 for p in range(1, h):
  offsetted = shift(normalized, (-p, 0))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
  if pruned.issubset(normalized):
   return p
 return h
TWO = 2
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def verify_task003(I):
 x0 = palette(I)
 x1 = other(x0, ZERO)
 x2 = ofcolor(I, x1)
 x3 = asobject(I)
 x4 = vperiod(x3)
 x5 = height(I)
 x6 = halve(x5)
 x7 = add(x5, x6)
 x8 = width(I)
 x9 = astuple(x7, x8)
 x10 = canvas(ZERO, x9)
 x11 = increment(x7)
 x12 = interval(ZERO, x11, x4)
 x13 = lbind(shift, x2)
 x14 = apply(toivec, x12)
 x15 = mapply(x13, x14)
 x16 = fill(x10, TWO, x15)
 return x16
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]