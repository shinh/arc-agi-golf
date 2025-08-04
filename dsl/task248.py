DOWN_LEFT = (1, -1)
ONE = 1
ORIGIN = (0, 0)
UNITY = (1, 1)
ZERO = 0
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def contained(value,container):
 return value in container
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
def llcorner(patch):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def corners(patch):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def divide(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def equality(a,b):
 return a == b
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
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
def hmirror(piece):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(x):
 return x
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def intersection(a,b):
 return a & b
def interval(start,stop,step):
 return tuple(range(start, stop, step))
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
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def pair(a,b):
 return tuple(zip(a, b))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def portrait(piece):
 return height(piece) > width(piece)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
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
def shoot(start,direction):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def toivec(i):
 return (i, 0)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def verify_task248(I):
 x0 = portrait(I)
 x1 = branch(x0, identity, dmirror)
 x2 = x1(I)
 x3 = asindices(x2)
 x4 = shoot(ORIGIN, UNITY)
 x5 = intersection(x4, x3)
 x6 = lrcorner(x5)
 x7 = shoot(x6, DOWN_LEFT)
 x8 = intersection(x7, x3)
 x9 = combine(x5, x8)
 x10 = llcorner(x9)
 x11 = remove(x10, x9)
 x12 = lbind(shift, x11)
 x13 = height(x11)
 x14 = lbind(multiply, x13)
 x15 = chain(x12, toivec, x14)
 x16 = height(x2)
 x17 = height(x11)
 x18 = divide(x16, x17)
 x19 = increment(x18)
 x20 = interval(ZERO, x19, ONE)
 x21 = mapply(x15, x20)
 x22 = rbind(contained, x21)
 x23 = sfilter(x3, x22)
 x24 = asindices(I)
 x25 = corners(x24)
 x26 = difference(x24, x25)
 x27 = toobject(x26, I)
 x28 = mostcolor(x27)
 x29 = palette(I)
 x30 = other(x29, x28)
 x31 = ulcorner(x3)
 x32 = index(x2, x31)
 x33 = equality(x32, x30)
 x34 = urcorner(x3)
 x35 = index(x2, x34)
 x36 = equality(x35, x30)
 x37 = llcorner(x3)
 x38 = index(x2, x37)
 x39 = equality(x38, x30)
 x40 = lrcorner(x3)
 x41 = index(x2, x40)
 x42 = equality(x41, x30)
 x43 = astuple(x33, x36)
 x44 = astuple(x39, x42)
 x45 = combine(x43, x44)
 x46 = vmirror(x23)
 x47 = astuple(x23, x46)
 x48 = hmirror(x23)
 x49 = hmirror(x46)
 x50 = astuple(x48, x49)
 x51 = combine(x47, x50)
 x52 = pair(x45, x51)
 x53 = sfilter(x52, first)
 x54 = mapply(last, x53)
 x55 = fill(x2, x30, x54)
 x56 = x1(x55)
 return x56
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]