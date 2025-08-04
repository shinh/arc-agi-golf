ONE = 1
ORIGIN = (0, 0)
UNITY = (1, 1)
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
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
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def ineighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def intersection(
 a,
 b
):
 return a & b
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
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
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def positive(
 x
):
 return x > 0
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
def size(
 container
):
 return len(container)
def verify_task370(I):
 x0 = fgpartition(I)
 x1 = argmax(x0, size)
 x2 = other(x0, x1)
 x3 = ineighbors(ORIGIN)
 x4 = height(x1)
 x5 = increment(x4)
 x6 = interval(ZERO, x5, ONE)
 x7 = lbind(intersection, x1)
 x8 = chain(positive, size, x7)
 x9 = lbind(shift, x1)
 x10 = rbind(multiply, UNITY)
 x11 = chain(x8, x9, x10)
 x12 = sfilter(x6, x11)
 x13 = maximum(x12)
 x14 = increment(x13)
 x15 = toindices(x2)
 x16 = lbind(intersection, x15)
 x17 = lbind(shift, x1)
 x18 = rbind(multiply, x14)
 x19 = chain(toindices, x17, x18)
 x20 = chain(size, x16, x19)
 x21 = argmax(x3, x20)
 x22 = shape(I)
 x23 = maximum(x22)
 x24 = increment(x23)
 x25 = interval(ONE, x24, ONE)
 x26 = lbind(shift, x1)
 x27 = multiply(x14, x21)
 x28 = lbind(multiply, x27)
 x29 = pair(x25, x25)
 x30 = apply(x28, x29)
 x31 = mapply(x26, x30)
 x32 = color(x2)
 x33 = recolor(x32, x31)
 x34 = paint(I, x33)
 return x34
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]