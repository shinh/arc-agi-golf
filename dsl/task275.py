ONE = 1
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
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def contained(value,container):
 return value in container
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(iterable):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(grid,n):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
def intersection(a,b):
 return a & b
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
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
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
def shape(piece):
 return (height(piece), width(piece))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def size(container):
 return len(container)
def vsplit(grid,n):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task275(I):
 x0 = lbind(contained, TWO)
 x1 = lbind(apply, numcolors)
 x2 = compose(x0, x1)
 x3 = lbind(apply, shape)
 x4 = chain(size, dedupe, x3)
 x5 = matcher(x4, ONE)
 x6 = compose(palette, first)
 x7 = compose(palette, last)
 x8 = fork(intersection, x6, x7)
 x9 = compose(size, x8)
 x10 = matcher(x9, ONE)
 x11 = lbind(contained, ONE)
 x12 = compose(minimum, shape)
 x13 = lbind(apply, x12)
 x14 = chain(flip, x11, x13)
 x15 = fork(add, x2, x5)
 x16 = fork(add, x10, x14)
 x17 = fork(add, x15, x16)
 x18 = vsplit(I, TWO)
 x19 = hsplit(I, TWO)
 x20 = astuple(x18, x19)
 x21 = argmax(x20, x17)
 x22 = argmin(x21, numcolors)
 x23 = argmax(x21, numcolors)
 x24 = palette(x22)
 x25 = palette(x23)
 x26 = intersection(x24, x25)
 x27 = first(x26)
 x28 = asindices(x22)
 x29 = ofcolor(x22, x27)
 x30 = difference(x28, x29)
 x31 = asobject(x23)
 x32 = matcher(first, x27)
 x33 = sfilter(x31, x32)
 x34 = difference(x31, x33)
 x35 = shape(x22)
 x36 = multiply(x35, x35)
 x37 = canvas(x27, x36)
 x38 = lbind(shift, x30)
 x39 = lbind(multiply, x35)
 x40 = chain(x38, x39, last)
 x41 = fork(recolor, first, x40)
 x42 = mapply(x41, x34)
 x43 = paint(x37, x42)
 return x43
def p(g):
 return [list(r)for r in verify_task275(tuple(tuple(r) for r in g))]