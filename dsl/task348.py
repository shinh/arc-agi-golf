EIGHT = 8
NEG_ONE = -1
NEG_TWO = -2
ONE = 1
TEN = 10
THREE = 3
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def astuple(a,b):
 return (a, b)
def chain(h,g,f):
 return lambda x: h(g(f(x)))
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
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def cmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def extract(container,condition):
 return next(e for e in container if condition(e))
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
def first(container):
 return next(iter(container))
def hmirror(piece):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def interval(start,stop,step):
 return tuple(range(start, stop, step))
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
def rapply(functions,value):
 return type(functions)(function(value) for function in functions)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def uppermost(patch):
 return min(i for i, j in toindices(patch))
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
def verify_task348(I):
 x0 = astuple(identity, dmirror)
 x1 = astuple(cmirror, hmirror)
 x2 = combine(x0, x1)
 x3 = chain(uppermost, merge, fgpartition)
 x4 = rbind(rapply, I)
 x5 = chain(first, x4, initset)
 x6 = compose(x3, x5)
 x7 = matcher(x6, ZERO)
 x8 = extract(x2, x7)
 x9 = x8(I)
 x10 = fgpartition(x9)
 x11 = merge(x10)
 x12 = width(x11)
 x13 = astuple(NEG_ONE, x12)
 x14 = invert(x12)
 x15 = astuple(NEG_ONE, x14)
 x16 = double(x12)
 x17 = astuple(NEG_TWO, x16)
 x18 = double(x12)
 x19 = invert(x18)
 x20 = astuple(NEG_TWO, x19)
 x21 = multiply(THREE, TEN)
 x22 = interval(ZERO, x21, ONE)
 x23 = lbind(multiply, x13)
 x24 = apply(x23, x22)
 x25 = lbind(multiply, x15)
 x26 = apply(x25, x22)
 x27 = lbind(multiply, x17)
 x28 = apply(x27, x22)
 x29 = lbind(multiply, x20)
 x30 = apply(x29, x22)
 x31 = lbind(shift, x11)
 x32 = mapply(x31, x24)
 x33 = lbind(shift, x11)
 x34 = mapply(x33, x26)
 x35 = lbind(shift, x11)
 x36 = mapply(x35, x28)
 x37 = lbind(shift, x11)
 x38 = mapply(x37, x30)
 x39 = combine(x32, x34)
 x40 = fill(x9, EIGHT, x39)
 x41 = combine(x36, x38)
 x42 = paint(x40, x41)
 x43 = x8(x42)
 return x43
def p(g):
 return [list(r)for r in verify_task348(tuple(tuple(r) for r in g))]