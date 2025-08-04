FIVE = 5
FOUR = 4
THREE = 3
TWO = 2
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def astuple(a,b):
 return (a, b)
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
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
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def size(container):
 return len(container)
def tojvec(j):
 return (0, j)
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task200(I):
 x0 = fgpartition(I)
 x1 = argmin(x0, size)
 x2 = color(x1)
 x3 = leftmost(x1)
 x4 = width(I)
 x5 = interval(x3, x4, TWO)
 x6 = apply(tojvec, x5)
 x7 = mapply(vfrontier, x6)
 x8 = fill(I, x2, x7)
 x9 = increment(x3)
 x10 = width(I)
 x11 = interval(x9, x10, FOUR)
 x12 = add(x3, THREE)
 x13 = width(I)
 x14 = interval(x12, x13, FOUR)
 x15 = apply(tojvec, x11)
 x16 = height(I)
 x17 = decrement(x16)
 x18 = lbind(astuple, x17)
 x19 = apply(x18, x14)
 x20 = combine(x15, x19)
 x21 = fill(x8, FIVE, x20)
 return x21
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]