def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def even(
 n
):
 return n % 2 == 0
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
def last(
 container
):
 return max(enumerate(container))[1]
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
def flip(
 b
):
 return not b
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def size(
 container
):
 return len(container)
def both(
 a,
 b
):
 return a and b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def color(
 obj
):
 return next(iter(obj))[0]
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
def verify_task085(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = fork(equality, size, x1)
 x3 = compose(flip, x2)
 x4 = extract(x0, x3)
 x5 = remove(x4, x0)
 x6 = compose(flip, even)
 x7 = rbind(chain, first)
 x8 = rbind(chain, last)
 x9 = lbind(rbind, subtract)
 x10 = lbind(x7, x6)
 x11 = lbind(x8, x6)
 x12 = chain(x10, x9, uppermost)
 x13 = chain(x11, x9, leftmost)
 x14 = lbind(fork, both)
 x15 = fork(x14, x12, x13)
 x16 = fork(sfilter, toindices, x15)
 x17 = mapply(x16, x5)
 x18 = color(x4)
 x19 = fill(I, x18, x17)
 return x19
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]