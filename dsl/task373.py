def apply(function,container):
 return type(container)(function(e) for e in container)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(a,b):
 return (a, b)
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def equality(a,b):
 return a == b
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def identity(x):
 return x
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
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def verify_task373(I):
 x0 = asobject(I)
 x1 = height(I)
 x2 = decrement(x1)
 x3 = lbind(subtract, x2)
 x4 = compose(double, halve)
 x5 = fork(equality, identity, x4)
 x6 = compose(last, last)
 x7 = chain(flip, x5, x6)
 x8 = sfilter(x0, x7)
 x9 = chain(x3, first, last)
 x10 = compose(last, last)
 x11 = fork(astuple, x9, x10)
 x12 = fork(astuple, first, x11)
 x13 = apply(x12, x8)
 x14 = paint(I, x13)
 return x14
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]