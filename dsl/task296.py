def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
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
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def frontiers(grid):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def matcher(function,target):
 return lambda x: function(x) == target
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task296(I):
 x0 = height(I)
 x1 = halve(x0)
 x2 = increment(x1)
 x3 = width(I)
 x4 = halve(x3)
 x5 = frontiers(I)
 x6 = merge(x5)
 x7 = mostcolor(x6)
 x8 = astuple(x2, x4)
 x9 = canvas(x7, x8)
 x10 = asindices(x9)
 x11 = toobject(x10, I)
 x12 = increment(x4)
 x13 = tojvec(x12)
 x14 = shift(x10, x13)
 x15 = toobject(x14, I)
 x16 = decrement(x2)
 x17 = toivec(x16)
 x18 = shift(x10, x17)
 x19 = toobject(x18, I)
 x20 = decrement(x2)
 x21 = increment(x4)
 x22 = astuple(x20, x21)
 x23 = shift(x10, x22)
 x24 = toobject(x23, I)
 x25 = palette(I)
 x26 = other(x25, x7)
 x27 = matcher(first, x26)
 x28 = rbind(sfilter, x27)
 x29 = chain(toindices, x28, normalize)
 x30 = x29(x11)
 x31 = x29(x15)
 x32 = x29(x19)
 x33 = x29(x24)
 x34 = combine(x30, x31)
 x35 = combine(x32, x33)
 x36 = combine(x34, x35)
 x37 = fill(x9, x26, x36)
 return x37
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]