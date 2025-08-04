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
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def color(obj):
 return next(iter(obj))[0]
def colorfilter(objs,value):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
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
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def frontiers(grid):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def adjacent(a,b):
 return manhattan(a, b) == 1
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
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def vmatching(a,b):
 return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0
def gravitate(source,destination):
 source_i, source_j = center(source)
 destination_i, destination_j = center(destination)
 i, j = 0, 0
 if vmatching(source, destination):
  i = 1 if source_i < destination_i else -1
 else:
  j = 1 if source_j < destination_j else -1
 direction = (i, j)
 gravitation_i, gravitation_j = i, j
 maxcount = 42
 c = 0
 while not adjacent(source, destination) and c < maxcount:
  c += 1
  gravitation_i += i
  gravitation_j += j
  source = shift(source, direction)
 return (gravitation_i - i, gravitation_j - j)
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def leastcommon(container):
 return min(set(container), key=container.count)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
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
def shape(piece):
 return (height(piece), width(piece))
def sign(x):
 if isinstance(x, int):
  return 0 if x == 0 else (1 if x > 0 else -1)
 return (0 if x[0] == 0 else (1 if x[0] > 0 else -1),0 if x[1] == 0 else (1 if x[1] > 0 else -1)
 )
def size(container):
 return len(container)
def totuple(container):
 return tuple(container)
def verify_task212(I):
 x0 = frontiers(I)
 x1 = totuple(x0)
 x2 = apply(color, x1)
 x3 = leastcommon(x2)
 x4 = frontiers(I)
 x5 = colorfilter(x4, x3)
 x6 = size(x5)
 x7 = positive(x6)
 x8 = branch(x7, dmirror, identity)
 x9 = ofcolor(I, x3)
 x10 = ofcolor(I, TWO)
 x11 = ofcolor(I, ONE)
 x12 = rbind(gravitate, x9)
 x13 = compose(x12, initset)
 x14 = fork(add, identity, x13)
 x15 = fork(connect, identity, x14)
 x16 = shape(I)
 x17 = maximum(x16)
 x18 = lbind(multiply, x17)
 x19 = lbind(gravitate, x9)
 x20 = chain(x18, sign, x19)
 x21 = compose(x20, initset)
 x22 = fork(add, identity, x21)
 x23 = fork(connect, identity, x22)
 x24 = mapply(x15, x10)
 x25 = mapply(x23, x11)
 x26 = fill(I, TWO, x24)
 x27 = fill(x26, ONE, x25)
 return x27
def p(g):
 return [list(r)for r in verify_task212(tuple(tuple(r) for r in g))]