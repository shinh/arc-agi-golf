F = False
ONE = 1
T = True
TWO = 2
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def divide(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def equality(a,b):
 return a == b
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
def first(container):
 return next(iter(container))
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
def hline(patch):
 return width(patch) == len(patch) and height(patch) == 1
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
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
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def mfilter(container,function):
 return merge(sfilter(container, function))
def mostcommon(container):
 return max(set(container), key=container.count)
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ineighbors(loc):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(loc):
 return dneighbors(loc) | ineighbors(loc)
def objects(grid,univalued,diagonal,without_bg):
 bg = mostcolor(grid) if without_bg else None
 objs = set()
 occupied = set()
 h, w = len(grid), len(grid[0])
 unvisited = asindices(grid)
 diagfun = neighbors if diagonal else dneighbors
 for loc in unvisited:
  if loc in occupied:
   continue
  val = grid[loc[0]][loc[1]]
  if val == bg:
   continue
  obj = {(val, loc)}
  cands = {loc}
  while len(cands) > 0:
   neighborhood = set()
   for cand in cands:
    v = grid[cand[0]][cand[1]]
    if (val == v) if univalued else (v != bg):
     obj.add((v, cand))
     occupied.add(cand)
     neighborhood |= {
      (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
     }
   cands = neighborhood - occupied
  objs.add(frozenset(obj))
 return frozenset(objs)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
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
def totuple(container):
 return tuple(container)
def vline(patch):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task358(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = compose(first, last)
 x3 = totuple(x1)
 x4 = apply(x2, x3)
 x5 = mostcommon(x4)
 x6 = compose(last, last)
 x7 = totuple(x1)
 x8 = apply(x6, x7)
 x9 = mostcommon(x8)
 x10 = compose(first, last)
 x11 = matcher(x10, x5)
 x12 = sfilter(x1, x11)
 x13 = compose(last, last)
 x14 = matcher(x13, x9)
 x15 = sfilter(x1, x14)
 x16 = objects(I, F, T, T)
 x17 = size(x16)
 x18 = equality(x17, TWO)
 x19 = mfilter(x16, hline)
 x20 = mfilter(x16, vline)
 x21 = branch(x18, x19, x12)
 x22 = branch(x18, x20, x15)
 x23 = width(x21)
 x24 = lbind(multiply, x23)
 x25 = width(I)
 x26 = divide(x25, x23)
 x27 = increment(x26)
 x28 = interval(ZERO, x27, ONE)
 x29 = apply(x24, x28)
 x30 = apply(invert, x29)
 x31 = combine(x29, x30)
 x32 = apply(tojvec, x31)
 x33 = lbind(shift, x21)
 x34 = mapply(x33, x32)
 x35 = height(x22)
 x36 = lbind(multiply, x35)
 x37 = height(I)
 x38 = height(x21)
 x39 = divide(x37, x38)
 x40 = increment(x39)
 x41 = interval(ZERO, x40, ONE)
 x42 = apply(x36, x41)
 x43 = apply(invert, x42)
 x44 = combine(x42, x43)
 x45 = apply(toivec, x44)
 x46 = lbind(shift, x22)
 x47 = mapply(x46, x45)
 x48 = combine(x34, x47)
 x49 = paint(I, x48)
 return x49
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]