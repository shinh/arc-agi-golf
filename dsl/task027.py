ONE = 1
TWO = 2
ZERO = 0
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
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
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
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
def center(patch):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def difference(a,b):
 return type(a)(e for e in a if e not in b)
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
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def intersection(a,b):
 return a & b
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def maximum(container):
 return max(container, default=0)
def minimum(container):
 return min(container, default=0)
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def normalize(patch):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def outbox(patch):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def power(function,n):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
def size(container):
 return len(container)
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def verify_task027(I):
 x0 = fgpartition(I)
 x1 = mapply(toindices, x0)
 x2 = rot90(I)
 x3 = fgpartition(x2)
 x4 = mapply(toindices, x3)
 x5 = normalize(x4)
 x6 = ulcorner(x1)
 x7 = shift(x5, x6)
 x8 = shape(x1)
 x9 = maximum(x8)
 x10 = minimum(x8)
 x11 = subtract(x9, x10)
 x12 = increment(x11)
 x13 = power(outbox, x12)
 x14 = center(x7)
 x15 = x13(x7)
 x16 = backdrop(x15)
 x17 = invert(x14)
 x18 = shift(x16, x17)
 x19 = lbind(combine, x1)
 x20 = lbind(shift, x7)
 x21 = compose(x19, x20)
 x22 = rbind(ofcolor, ONE)
 x23 = lbind(canvas, ZERO)
 x24 = chain(x23, shape, x21)
 x25 = lbind(recolor, ONE)
 x26 = chain(x25, normalize, x21)
 x27 = fork(paint, x24, x26)
 x28 = chain(x22, rot90, x27)
 x29 = compose(normalize, x21)
 x30 = fork(equality, x29, x28)
 x31 = sfilter(x18, x30)
 x32 = lbind(intersection, x1)
 x33 = lbind(shift, x7)
 x34 = chain(size, x32, x33)
 x35 = argmax(x31, x34)
 x36 = shift(x7, x35)
 x37 = difference(x36, x1)
 x38 = fill(I, TWO, x37)
 return x38
def p(g):
 return [list(r)for r in verify_task027(tuple(tuple(r) for r in g))]