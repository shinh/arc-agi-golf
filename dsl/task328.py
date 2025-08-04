F = False
NEG_ONE = -1
ONE = 1
T = True
TEN = 10
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
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def greater(a,b):
 return a > b
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def intersection(a,b):
 return a & b
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
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def maximum(container):
 return max(container, default=0)
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
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def outbox(patch):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def pair(a,b):
 return tuple(zip(a, b))
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
def remove(value,container):
 return type(container)(e for e in container if e != value)
def repeat(item,num):
 return tuple(item for i in range(num))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
def totuple(container):
 return tuple(container)
def verify_task328(I):
 x0 = objects(I, T, F, T)
 x1 = totuple(x0)
 x2 = apply(color, x1)
 x3 = repeat(NEG_ONE, ONE)
 x4 = combine(x2, x3)
 x5 = multiply(TEN, TEN)
 x6 = apply(center, x1)
 x7 = astuple(x5, x5)
 x8 = repeat(x7, ONE)
 x9 = combine(x6, x8)
 x10 = identity(I)
 x11 = asindices(I)
 x12 = shape(I)
 x13 = maximum(x12)
 x14 = halve(x13)
 x15 = add(TWO, x14)
 x16 = interval(ONE, x15, ONE)
 x17 = compose(outbox, outbox)
 x18 = lbind(power, x17)
 x19 = apply(x18, x16)
 x20 = lbind(rapply, x19)
 x21 = chain(merge, x20, initset)
 x22 = fork(combine, initset, x21)
 x23 = lbind(rbind, manhattan)
 x24 = rbind(chain, initset)
 x25 = rbind(x24, x23)
 x26 = lbind(rbind, apply)
 x27 = lbind(apply, initset)
 x28 = rbind(remove, x9)
 x29 = chain(x25, x26, x27)
 x30 = chain(x29, x28, last)
 x31 = lbind(sfilter, x11)
 x32 = rbind(compose, initset)
 x33 = lbind(compose, minimum)
 x34 = lbind(fork, greater)
 x35 = compose(x33, x30)
 x36 = compose(initset, last)
 x37 = chain(x32, x23, x36)
 x38 = fork(x34, x35, x37)
 x39 = compose(x31, x38)
 x40 = compose(x22, last)
 x41 = fork(intersection, x39, x40)
 x42 = fork(recolor, first, x41)
 x43 = pair(x4, x9)
 x44 = mapply(x42, x43)
 x45 = paint(x10, x44)
 return x45
def p(g):
 return [list(r)for r in verify_task328(tuple(tuple(r) for r in g))]