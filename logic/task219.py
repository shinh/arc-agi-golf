ONE = 1
ZERO = 0
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
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
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
def compose(outer,inner):
 return lambda x: outer(inner(x))
def contained(value,container):
 return value in container
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def greater(a,b):
 return a > b
def identity(x):
 return x
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def insert(value,container):
 return container.union(frozenset({value}))
def intersection(a,b):
 return a & b
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
def leastcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def maximum(container):
 return max(container, default=0)
def minimum(container):
 return min(container, default=0)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def positive(x):
 return x > 0
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
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
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def valmax(container,compfunc):
 return compfunc(max(container, key=compfunc, default=0))
def verify_task219(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = apply(first, x1)
 x3 = asindices(I)
 x4 = apply(first, x3)
 x5 = difference(x4, x2)
 x6 = ofcolor(I, x0)
 x7 = rbind(interval, ONE)
 x8 = lbind(rbind, contained)
 x9 = lbind(sfilter, x5)
 x10 = rbind(matcher, ZERO)
 x11 = chain(size, x9, x8)
 x12 = lbind(sfilter, x6)
 x13 = lbind(compose, x11)
 x14 = chain(x12, x10, x13)
 x15 = lbind(fork, x7)
 x16 = compose(increment, minimum)
 x17 = lbind(lbind, astuple)
 x18 = lbind(chain, x16)
 x19 = rbind(x18, first)
 x20 = chain(x19, x17, first)
 x21 = lbind(chain, maximum)
 x22 = rbind(x21, first)
 x23 = chain(x22, x17, first)
 x24 = fork(x15, x20, x23)
 x25 = compose(x14, x24)
 x26 = apply(toivec, x2)
 x27 = apply(x25, x26)
 x28 = argmax(x27, width)
 x29 = remove(x28, x27)
 x30 = ulcorner(x28)
 x31 = invert(x30)
 x32 = shift(x28, x31)
 x33 = asindices(I)
 x34 = center(x33)
 x35 = invert(x34)
 x36 = shift(x33, x35)
 x37 = width(I)
 x38 = double(x37)
 x39 = tojvec(x38)
 x40 = rbind(apply, x36)
 x41 = lbind(rbind, add)
 x42 = chain(x40, x41, center)
 x43 = compose(positive, size)
 x44 = lbind(compose, size)
 x45 = lbind(shift, x32)
 x46 = rbind(compose, x45)
 x47 = lbind(rbind, intersection)
 x48 = compose(x46, x47)
 x49 = lbind(compose, x43)
 x50 = compose(x49, x48)
 x51 = fork(sfilter, x42, x50)
 x52 = compose(x44, x48)
 x53 = fork(valmax, x51, x52)
 x54 = compose(x44, x48)
 x55 = fork(matcher, x54, x53)
 x56 = fork(sfilter, x51, x55)
 x57 = lbind(shift, x32)
 x58 = lbind(insert, x39)
 x59 = lbind(rbind, greater)
 x60 = compose(x59, rightmost)
 x61 = compose(leftmost, x58)
 x62 = rbind(compose, x57)
 x63 = lbind(rbind, difference)
 x64 = compose(x62, x63)
 x65 = lbind(compose, x61)
 x66 = compose(x65, x64)
 x67 = fork(compose, x60, x66)
 x68 = fork(argmax, x56, x67)
 x69 = lbind(shift, x32)
 x70 = compose(x69, x68)
 x71 = fork(difference, x70, identity)
 x72 = mapply(x71, x29)
 x73 = fill(I, ONE, x72)
 return x73
def p(g):
 return [list(r)for r in verify_task219(tuple(tuple(r) for r in g))]