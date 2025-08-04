ONE = 1
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(a,b):
 return (a, b)
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def contained(value,container):
 return value in container
def divide(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def first(container):
 return next(iter(container))
def flip(b):
 return not b
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
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def hperiod(obj):
 normalized = normalize(obj)
 w = width(normalized)
 for p in range(1, w):
  offsetted = shift(normalized, (0, -p))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
  if pruned.issubset(normalized):
   return p
 return w
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(grid,n):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
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
def minimum(container):
 return min(container, default=0)
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
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def product(a,b):
 return frozenset((i, j) for j in b for i in a)
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
def vperiod(obj):
 normalized = normalize(obj)
 h = height(normalized)
 for p in range(1, h):
  offsetted = shift(normalized, (-p, 0))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
  if pruned.issubset(normalized):
   return p
 return h
def vsplit(grid,n):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task305(I):
 x0 = height(I)
 x1 = vsplit(I, x0)
 x2 = apply(asobject, x1)
 x3 = apply(hperiod, x2)
 x4 = minimum(x3)
 x5 = width(I)
 x6 = hsplit(I, x5)
 x7 = apply(asobject, x6)
 x8 = apply(vperiod, x7)
 x9 = minimum(x8)
 x10 = matcher(hperiod, x4)
 x11 = sfilter(x2, x10)
 x12 = mapply(palette, x11)
 x13 = matcher(vperiod, x9)
 x14 = sfilter(x7, x13)
 x15 = mapply(palette, x14)
 x16 = palette(I)
 x17 = combine(x12, x15)
 x18 = rbind(contained, x17)
 x19 = argmin(x16, x18)
 x20 = asobject(I)
 x21 = matcher(first, x19)
 x22 = compose(flip, x21)
 x23 = sfilter(x20, x22)
 x24 = height(I)
 x25 = divide(x24, x9)
 x26 = increment(x25)
 x27 = width(I)
 x28 = divide(x27, x4)
 x29 = increment(x28)
 x30 = invert(x26)
 x31 = interval(x30, x26, ONE)
 x32 = invert(x29)
 x33 = interval(x32, x29, ONE)
 x34 = product(x31, x33)
 x35 = astuple(x9, x4)
 x36 = lbind(multiply, x35)
 x37 = apply(x36, x34)
 x38 = lbind(shift, x23)
 x39 = mapply(x38, x37)
 x40 = paint(I, x39)
 return x40
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]