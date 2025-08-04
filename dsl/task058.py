DOWN = (1, 0)
F = False
LEFT = (0, -1)
ONE = 1
ORIGIN = (0, 0)
RIGHT = (0, 1)
TEN = 10
THREE = 3
UP = (-1, 0)
ZERO = 0
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def astuple(a,b):
 return (a, b)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
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
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
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
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def extract(container,condition):
 return next(e for e in container if condition(e))
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
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
def initset(value):
 return frozenset({value})
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
def positive(x):
 return x > 0
def power(function,n):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
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
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
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
def tojvec(j):
 return (0, j)
def verify_task058(I):
 x0 = astuple(RIGHT, DOWN)
 x1 = astuple(DOWN, LEFT)
 x2 = astuple(x0, x1)
 x3 = astuple(LEFT, UP)
 x4 = astuple(UP, RIGHT)
 x5 = astuple(x3, x4)
 x6 = combine(x2, x5)
 x7 = height(I)
 x8 = astuple(x7, ONE)
 x9 = canvas(THREE, x8)
 x10 = hconcat(x9, I)
 x11 = height(x10)
 x12 = width(x10)
 x13 = decrement(x12)
 x14 = tojvec(x13)
 x15 = identity(DOWN)
 x16 = connect(ORIGIN, x14)
 x17 = fill(x10, THREE, x16)
 x18 = identity(x12)
 x19 = identity(x11)
 x20 = identity(x11)
 x21 = identity(F)
 x22 = identity(ZERO)
 x23 = compose(first, first)
 x24 = chain(first, last, x23)
 x25 = compose(first, first)
 x26 = chain(last, last, x25)
 x27 = chain(first, first, first)
 x28 = chain(first, last, last)
 x29 = chain(first, first, last)
 x30 = chain(last, first, last)
 x31 = compose(decrement, x24)
 x32 = compose(decrement, x26)
 x33 = fork(astuple, x31, x32)
 x34 = compose(decrement, x26)
 x35 = fork(multiply, x29, x34)
 x36 = fork(add, x28, x35)
 x37 = compose(decrement, x27)
 x38 = fork(multiply, x29, x37)
 x39 = fork(add, x28, x38)
 x40 = fork(astuple, x39, x36)
 x41 = lbind(extract, x6)
 x42 = lbind(matcher, first)
 x43 = compose(x42, x29)
 x44 = chain(last, x41, x43)
 x45 = compose(last, first)
 x46 = lbind(recolor, THREE)
 x47 = compose(decrement, x27)
 x48 = fork(multiply, x29, x47)
 x49 = fork(add, x28, x48)
 x50 = fork(connect, x28, x49)
 x51 = compose(x46, x50)
 x52 = fork(paint, x45, x51)
 x53 = compose(decrement, x26)
 x54 = fork(multiply, x30, x53)
 x55 = compose(flip, x30)
 x56 = compose(decrement, x24)
 x57 = fork(multiply, x55, x56)
 x58 = fork(add, x54, x57)
 x59 = power(first, THREE)
 x60 = chain(flip, positive, x59)
 x61 = fork(astuple, x58, x33)
 x62 = compose(flip, x30)
 x63 = fork(astuple, x44, x62)
 x64 = fork(astuple, x61, x52)
 x65 = fork(astuple, x63, x40)
 x66 = fork(astuple, x64, x65)
 x67 = rbind(branch, x66)
 x68 = rbind(x67, identity)
 x69 = chain(initset, x68, x60)
 x70 = fork(rapply, x69, identity)
 x71 = compose(first, x70)
 x72 = multiply(TEN, THREE)
 x73 = power(x71, x72)
 x74 = astuple(x18, x19)
 x75 = astuple(x15, x21)
 x76 = astuple(x14, x22)
 x77 = astuple(x20, x74)
 x78 = astuple(x75, x76)
 x79 = astuple(x77, x17)
 x80 = astuple(x79, x78)
 x81 = x73(x80)
 x82 = first(x81)
 x83 = last(x82)
 x84 = dmirror(x83)
 x85 = shape(x84)
 x86 = add(x85, UP)
 x87 = crop(x84, DOWN, x86)
 x88 = dmirror(x87)
 return x88
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]