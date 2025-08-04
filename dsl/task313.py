DOWN = (1, 0)
LEFT = (0, -1)
ONE = 1
ORIGIN = (0, 0)
RIGHT = (0, 1)
TWO = 2
UP = (-1, 0)
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def box(
 patch
):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def equality(
 a,
 b
):
 return a == b
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
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
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
def verify_task313(I):
 x0 = asindices(I)
 x1 = box(x0)
 x2 = toobject(x1, I)
 x3 = mostcolor(x2)
 x4 = asobject(I)
 x5 = matcher(first, x3)
 x6 = compose(flip, x5)
 x7 = sfilter(x4, x6)
 x8 = hperiod(x7)
 x9 = vperiod(x7)
 x10 = width(I)
 x11 = width(x7)
 x12 = subtract(x10, x11)
 x13 = add(x12, TWO)
 x14 = height(I)
 x15 = height(x7)
 x16 = subtract(x14, x15)
 x17 = add(x16, TWO)
 x18 = rbind(multiply, x8)
 x19 = invert(x13)
 x20 = interval(x19, x13, ONE)
 x21 = apply(x18, x20)
 x22 = rbind(multiply, x9)
 x23 = invert(x17)
 x24 = interval(x23, x17, ONE)
 x25 = apply(x22, x24)
 x26 = product(x25, x21)
 x27 = lbind(shift, x7)
 x28 = mapply(x27, x26)
 x29 = index(I, ORIGIN)
 x30 = equality(x29, x3)
 x31 = flip(x30)
 x32 = asindices(I)
 x33 = urcorner(x32)
 x34 = index(I, x33)
 x35 = equality(x34, x3)
 x36 = flip(x35)
 x37 = asindices(I)
 x38 = lrcorner(x37)
 x39 = index(I, x38)
 x40 = equality(x39, x3)
 x41 = flip(x40)
 x42 = asindices(I)
 x43 = llcorner(x42)
 x44 = index(I, x43)
 x45 = equality(x44, x3)
 x46 = flip(x45)
 x47 = multiply(x31, LEFT)
 x48 = multiply(x36, UP)
 x49 = add(x47, x48)
 x50 = multiply(x41, RIGHT)
 x51 = multiply(x46, DOWN)
 x52 = add(x50, x51)
 x53 = add(x49, x52)
 x54 = shift(x28, x53)
 x55 = paint(I, x54)
 return x55
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]