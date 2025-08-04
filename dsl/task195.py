def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def shape(
 piece
):
 return (height(piece), width(piece))
def pair(
 a,
 b
):
 return tuple(zip(a, b))
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
ONE = 1
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def last(
 container
):
 return max(enumerate(container))[1]
def equality(
 a,
 b
):
 return a == b
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
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
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
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
def color(
 obj
):
 return next(iter(obj))[0]
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
def verify_task195(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = argmin(x0, x1)
 x3 = color(x2)
 x4 = palette(I)
 x5 = other(x4, x3)
 x6 = subgrid(x2, I)
 x7 = fork(multiply, identity, identity)
 x8 = width(x6)
 x9 = matcher(x7, x8)
 x10 = fork(multiply, identity, identity)
 x11 = height(x6)
 x12 = matcher(x10, x11)
 x13 = width(x6)
 x14 = interval(ONE, x13, ONE)
 x15 = extract(x14, x9)
 x16 = height(x6)
 x17 = interval(ONE, x16, ONE)
 x18 = extract(x17, x12)
 x19 = width(x6)
 x20 = interval(ZERO, x19, ONE)
 x21 = height(x6)
 x22 = interval(ZERO, x21, ONE)
 x23 = rbind(multiply, x15)
 x24 = rbind(divide, x15)
 x25 = compose(x23, x24)
 x26 = fork(equality, identity, x25)
 x27 = compose(x26, last)
 x28 = rbind(multiply, x18)
 x29 = rbind(divide, x18)
 x30 = compose(x28, x29)
 x31 = fork(equality, identity, x30)
 x32 = compose(x31, last)
 x33 = lbind(apply, first)
 x34 = rbind(sfilter, x27)
 x35 = rbind(pair, x20)
 x36 = chain(x33, x34, x35)
 x37 = pair(x6, x22)
 x38 = sfilter(x37, x32)
 x39 = apply(first, x38)
 x40 = apply(x36, x39)
 x41 = shape(x40)
 x42 = multiply(x41, x41)
 x43 = canvas(x5, x42)
 x44 = ofcolor(x40, x3)
 x45 = rbind(multiply, x41)
 x46 = apply(x45, x44)
 x47 = lbind(shift, x44)
 x48 = mapply(x47, x46)
 x49 = fill(x43, x3, x48)
 return x49
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]