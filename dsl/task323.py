DOWN = (1, 0)
FIVE = 5
NEG_TWO = -2
ONE = 1
ORIGIN = (0, 0)
TEN = 10
TWO = 2
TWO_BY_ZERO = (2, 0)
ZERO = 0
ZERO_BY_TWO = (0, 2)
def apply(function,container):
 return type(container)(function(e) for e in container)
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def connect(a,b):
 ai, aj = a
 bi, bj = b
 si = min(ai, bi)
 ei = max(ai, bi) + 1
 sj = min(aj, bj)
 ej = max(aj, bj) + 1
 if ai == bi:
  return frozenset((ai, j) for j in range(sj, ej))
 elif aj == bj:
  return frozenset((i, aj) for i in range(si, ei))
 elif bi - ai == bj - aj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
 elif bi - ai == aj - bj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
 return frozenset()
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def leastcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
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
def shape(piece):
 return (height(piece), width(piece))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def toivec(i):
 return (i, 0)
def verify_task323(I):
 x0 = double(TEN)
 x1 = interval(ZERO, x0, ONE)
 x2 = connect(ORIGIN, DOWN)
 x3 = connect(ORIGIN, ZERO_BY_TWO)
 x4 = combine(x2, x3)
 x5 = astuple(NEG_TWO, TWO)
 x6 = lbind(multiply, x5)
 x7 = toivec(NEG_TWO)
 x8 = apply(x6, x1)
 x9 = rbind(subtract, TWO_BY_ZERO)
 x10 = fork(ofcolor, identity, leastcolor)
 x11 = chain(x9, center, x10)
 x12 = rbind(mapply, x8)
 x13 = lbind(lbind, shift)
 x14 = lbind(shift, x4)
 x15 = compose(x14, x11)
 x16 = chain(x12, x13, x15)
 x17 = lbind(recolor, FIVE)
 x18 = compose(x17, x16)
 x19 = fork(paint, identity, x18)
 x20 = compose(rot180, x19)
 x21 = fork(ofcolor, x20, leastcolor)
 x22 = compose(center, x21)
 x23 = fork(subtract, x22, x11)
 x24 = fork(shift, x16, x23)
 x25 = lbind(recolor, FIVE)
 x26 = rbind(shift, x7)
 x27 = chain(x25, x26, x24)
 x28 = fork(paint, x20, x27)
 x29 = compose(rot180, x28)
 x30 = rbind(ofcolor, FIVE)
 x31 = compose(x30, x29)
 x32 = leastcolor(I)
 x33 = ofcolor(I, x32)
 x34 = mostcolor(I)
 x35 = shape(I)
 x36 = canvas(x34, x35)
 x37 = lbind(paint, x36)
 x38 = lbind(recolor, x32)
 x39 = chain(x37, x38, initset)
 x40 = compose(x31, x39)
 x41 = mapply(x40, x33)
 x42 = fill(I, FIVE, x41)
 x43 = fill(x42, x32, x33)
 return x43
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]