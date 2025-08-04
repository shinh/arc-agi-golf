DOWN = (1, 0)
NEG_UNITY = (-1, -1)
ONE = 1
RIGHT = (0, 1)
UP_RIGHT = (-1, 1)
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def astuple(a,b):
 return (a, b)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def divide(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def greater(a,b):
 return a > b
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
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def pair(a,b):
 return tuple(zip(a, b))
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
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
def size(container):
 return len(container)
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def valmax(container,compfunc):
 return compfunc(max(container, key=compfunc, default=0))
def verify_task007(I):
 x0 = shape(I)
 x1 = maximum(x0)
 x2 = interval(ZERO, x1, ONE)
 x3 = interval(ONE, x1, ONE)
 x4 = rbind(toobject, I)
 x5 = rbind(shoot, RIGHT)
 x6 = chain(x4, x5, toivec)
 x7 = rbind(shoot, DOWN)
 x8 = chain(x4, x7, tojvec)
 x9 = apply(x6, x2)
 x10 = apply(x8, x2)
 x11 = rbind(shoot, UP_RIGHT)
 x12 = chain(x4, x11, toivec)
 x13 = rbind(shoot, UP_RIGHT)
 x14 = decrement(x1)
 x15 = lbind(astuple, x14)
 x16 = chain(x4, x13, x15)
 x17 = apply(x12, x2)
 x18 = apply(x16, x3)
 x19 = combine(x17, x18)
 x20 = rbind(shoot, NEG_UNITY)
 x21 = decrement(x1)
 x22 = lbind(astuple, x21)
 x23 = chain(x4, x20, x22)
 x24 = rbind(shoot, NEG_UNITY)
 x25 = decrement(x1)
 x26 = rbind(astuple, x25)
 x27 = lbind(subtract, x25)
 x28 = compose(x26, x27)
 x29 = chain(x4, x24, x28)
 x30 = apply(x23, x2)
 x31 = apply(x29, x3)
 x32 = combine(x30, x31)
 x33 = rbind(valmax, numcolors)
 x34 = matcher(x33, ONE)
 x35 = x34(x9)
 x36 = x34(x10)
 x37 = x34(x19)
 x38 = branch(x37, x19, x32)
 x39 = branch(x36, x10, x38)
 x40 = branch(x35, x9, x39)
 x41 = apply(mostcolor, x40)
 x42 = matcher(identity, ZERO)
 x43 = compose(flip, x42)
 x44 = sfilter(x41, x43)
 x45 = size(x44)
 x46 = double(x1)
 x47 = divide(x46, x45)
 x48 = increment(x47)
 x49 = interval(ZERO, x48, ONE)
 x50 = matcher(first, ZERO)
 x51 = compose(flip, x50)
 x52 = fork(recolor, first, last)
 x53 = size(x40)
 x54 = interval(ZERO, x53, ONE)
 x55 = rbind(compose, first)
 x56 = lbind(rbind, greater)
 x57 = chain(x55, x56, decrement)
 x58 = lbind(apply, last)
 x59 = lbind(chain, x58)
 x60 = rbind(x59, x57)
 x61 = lbind(lbind, sfilter)
 x62 = lbind(pair, x54)
 x63 = chain(x60, x61, x62)
 x64 = x63(x40)
 x65 = x63(x41)
 x66 = rbind(multiply, x45)
 x67 = compose(x64, x66)
 x68 = rbind(multiply, x45)
 x69 = compose(x65, x68)
 x70 = lbind(mapply, x52)
 x71 = rbind(sfilter, x51)
 x72 = lbind(pair, x41)
 x73 = compose(x72, x67)
 x74 = chain(x70, x71, x73)
 x75 = lbind(mapply, x52)
 x76 = rbind(sfilter, x51)
 x77 = rbind(pair, x40)
 x78 = compose(x77, x69)
 x79 = chain(x75, x76, x78)
 x80 = fork(combine, x74, x79)
 x81 = mapply(x80, x49)
 x82 = paint(I, x81)
 return x82
def p(g):
 return [list(r)for r in verify_task007(tuple(tuple(r) for r in g))]