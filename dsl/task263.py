ONE = 1
TEN = 10
THREE = 3
TWO = 2
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
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
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
def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def equality(
 a,
 b
):
 return a == b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(
 grid,
 n
):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def mostcommon(
 container
):
 return max(set(container), key=container.count)
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
def size(
 container
):
 return len(container)
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task263(I):
 x0 = height(I)
 x1 = halve(x0)
 x2 = increment(x1)
 x3 = interval(THREE, x2, ONE)
 x4 = width(I)
 x5 = halve(x4)
 x6 = increment(x5)
 x7 = interval(THREE, x6, ONE)
 x8 = palette(I)
 x9 = lbind(apply, toindices)
 x10 = compose(x9, partition)
 x11 = rbind(compose, palette)
 x12 = lbind(lbind, contained)
 x13 = compose(x11, x12)
 x14 = lbind(chain, size)
 x15 = rbind(x14, x13)
 x16 = lbind(lbind, sfilter)
 x17 = compose(x15, x16)
 x18 = compose(positive, size)
 x19 = lbind(sfilter, x8)
 x20 = fork(matcher, x17, size)
 x21 = chain(x18, x19, x20)
 x22 = lbind(apply, shape)
 x23 = chain(size, dedupe, x22)
 x24 = matcher(x23, ONE)
 x25 = lbind(apply, x10)
 x26 = chain(size, dedupe, x25)
 x27 = matcher(x26, TWO)
 x28 = compose(size, dedupe)
 x29 = fork(equality, size, x28)
 x30 = fork(add, x21, x24)
 x31 = fork(add, x27, x29)
 x32 = fork(add, x30, x31)
 x33 = multiply(TEN, TEN)
 x34 = lbind(multiply, x33)
 x35 = compose(x34, x32)
 x36 = fork(add, x35, size)
 x37 = lbind(vsplit, I)
 x38 = apply(x37, x3)
 x39 = lbind(hsplit, I)
 x40 = apply(x39, x7)
 x41 = combine(x38, x40)
 x42 = argmax(x41, x36)
 x43 = apply(x10, x42)
 x44 = mostcommon(x43)
 x45 = matcher(x10, x44)
 x46 = argmin(x42, x45)
 return x46
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]