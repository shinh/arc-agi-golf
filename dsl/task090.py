NEG_ONE = -1
ONE = 1
SIX = 6
TWO = 2
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def difference(a,b):
 return type(a)(e for e in a if e not in b)
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
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def identity(x):
 return x
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
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
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def maximum(container):
 return max(container, default=0)
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
F = False
T = True
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def normalize(patch):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def occurrences(grid,obj):
 occurrences = set()
 normed = normalize(obj)
 h, w = len(grid), len(grid[0])
 for i in range(h):
  for j in range(w):
   occurs = True
   for v, (a, b) in shift(normed, (i, j)):
    if 0 <= a < h and 0 <= b < w:
     if grid[a][b] != v:
      occurs = False
      break
    else:
     occurs = False
     break
   if occurs:
    occurrences.add((i, j))
 return frozenset(occurrences)
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
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def size(container):
 return len(container)
def verify_task090(I):
 x0 = matcher(identity, ZERO)
 x1 = rbind(sfilter, x0)
 x2 = compose(size, x1)
 x3 = apply(x2, I)
 x4 = maximum(x3)
 x5 = dmirror(I)
 x6 = apply(x2, x5)
 x7 = maximum(x6)
 x8 = increment(x7)
 x9 = interval(TWO, x8, ONE)
 x10 = increment(x4)
 x11 = interval(TWO, x10, ONE)
 x12 = product(x9, x11)
 x13 = fork(multiply, first, last)
 x14 = apply(x13, x12)
 x15 = lbind(sfilter, x12)
 x16 = lbind(matcher, x13)
 x17 = compose(x15, x16)
 x18 = apply(x17, x14)
 x19 = lbind(occurrences, I)
 x20 = lbind(recolor, ZERO)
 x21 = lbind(canvas, NEG_ONE)
 x22 = compose(asindices, x21)
 x23 = chain(x19, x20, x22)
 x24 = lbind(mapply, x23)
 x25 = chain(positive, size, x24)
 x26 = sfilter(x18, x25)
 x27 = compose(x13, first)
 x28 = rbind(argmax, x27)
 x29 = lbind(recolor, ZERO)
 x30 = lbind(canvas, NEG_ONE)
 x31 = chain(x29, asindices, x30)
 x32 = lbind(lbind, shift)
 x33 = lbind(occurrences, I)
 x34 = fork(mapply, x32, x33)
 x35 = compose(x34, x31)
 x36 = size(x26)
 x37 = positive(x36)
 x38 = lbind(recolor, SIX)
 x39 = lbind(mapply, x35)
 x40 = chain(x38, x39, x28)
 x41 = fork(difference, identity, identity)
 x42 = branch(x37, x40, x41)
 x43 = x42(x26)
 x44 = paint(I, x43)
 return x44
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]