ONE = 1
ORIGIN = (0, 0)
SIX = 6
TEN = 10
ZERO = 0
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def astuple(a,b):
 return (a, b)
def both(a,b):
 return a and b
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def equality(a,b):
 return a == b
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def intersection(a,b):
 return a & b
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def last(container):
 return max(enumerate(container))[1]
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def positive(x):
 return x > 0
def product(a,b):
 return frozenset((i, j) for j in b for i in a)
def remove(value,container):
 return type(container)(e for e in container if e != value)
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def size(container):
 return len(container)
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def valmax(container,compfunc):
 return compfunc(max(container, key=compfunc, default=0))
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task124(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = mostcolor(I)
 x3 = width(I)
 x4 = astuple(TEN, x3)
 x5 = canvas(x2, x4)
 x6 = interval(ONE, SIX, ONE)
 x7 = invert(TEN)
 x8 = interval(x7, TEN, ONE)
 x9 = product(x6, x8)
 x10 = remove(ORIGIN, x9)
 x11 = lbind(intersection, x1)
 x12 = lbind(shift, x1)
 x13 = compose(x11, x12)
 x14 = toindices(x1)
 x15 = lbind(intersection, x14)
 x16 = lbind(shift, x14)
 x17 = compose(x15, x16)
 x18 = compose(size, x13)
 x19 = compose(size, x17)
 x20 = fork(equality, x18, x19)
 x21 = chain(positive, size, x13)
 x22 = fork(both, x20, x21)
 x23 = sfilter(x10, x22)
 x24 = compose(size, x13)
 x25 = valmax(x23, x24)
 x26 = compose(size, x13)
 x27 = matcher(x26, x25)
 x28 = sfilter(x23, x27)
 x29 = fork(multiply, first, last)
 x30 = argmax(x28, x29)
 x31 = interval(ZERO, TEN, ONE)
 x32 = lbind(shift, x1)
 x33 = lbind(multiply, x30)
 x34 = compose(x32, x33)
 x35 = mapply(x34, x31)
 x36 = paint(x5, x35)
 return x36
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]