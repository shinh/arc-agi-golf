EIGHT = 8
ONE = 1
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def extract(container,condition):
 return next(e for e in container if condition(e))
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def matcher(function,target):
 return lambda x: function(x) == target
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def papply(function,a,b):
 return tuple(function(i, j) for i, j in zip(a, b))
def mpapply(function,a,b):
 return merge(papply(function, a, b))
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
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def order(container,compfunc):
 return tuple(sorted(container, key=compfunc))
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def pair(a,b):
 return tuple(zip(a, b))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
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
def size(container):
 return len(container)
def toivec(i):
 return (i, 0)
def verify_task301(I):
 x0 = astuple(identity, rot90)
 x1 = astuple(rot180, rot270)
 x2 = combine(x0, x1)
 x3 = astuple(identity, rot270)
 x4 = astuple(rot180, rot90)
 x5 = combine(x3, x4)
 x6 = pair(x2, x5)
 x7 = rbind(rapply, I)
 x8 = compose(initset, first)
 x9 = chain(first, x7, x8)
 x10 = rbind(ofcolor, EIGHT)
 x11 = chain(lowermost, x10, x9)
 x12 = matcher(x11, ZERO)
 x13 = extract(x6, x12)
 x14 = first(x13)
 x15 = last(x13)
 x16 = x14(I)
 x17 = rot180(x16)
 x18 = shape(x17)
 x19 = lbind(apply, first)
 x20 = lbind(ofcolor, x17)
 x21 = chain(size, x19, x20)
 x22 = palette(I)
 x23 = argmax(x22, x21)
 x24 = partition(x17)
 x25 = matcher(color, x23)
 x26 = compose(flip, x25)
 x27 = sfilter(x24, x26)
 x28 = compose(invert, size)
 x29 = order(x27, x28)
 x30 = apply(normalize, x29)
 x31 = size(x30)
 x32 = interval(ZERO, x31, ONE)
 x33 = apply(toivec, x32)
 x34 = mpapply(shift, x30, x33)
 x35 = canvas(x23, x18)
 x36 = paint(x35, x34)
 x37 = x15(x36)
 return x37
def p(g):
 return [list(r)for r in verify_task301(tuple(tuple(r) for r in g))]