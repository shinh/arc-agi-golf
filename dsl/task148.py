F = False
FOUR = 4
ONE = 1
T = True
TWO = 2
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
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def both(a,b):
 return a and b
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
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def box(patch):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
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
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def either(a,b):
 return a or b
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
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
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
def greater(a,b):
 return a > b
def hfrontier(location):
 return frozenset((location[0], j) for j in range(30))
def hmatching(a,b):
 return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0
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
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def minimum(container):
 return min(container, default=0)
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
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
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
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def verify_task148(I):
 x0 = objects(I, T, F, T)
 x1 = merge(x0)
 x2 = palette(x1)
 x3 = lbind(colorfilter, x0)
 x4 = compose(size, x3)
 x5 = matcher(x4, TWO)
 x6 = asindices(I)
 x7 = box(x6)
 x8 = rbind(difference, x7)
 x9 = lbind(ofcolor, I)
 x10 = chain(size, x8, x9)
 x11 = matcher(x10, ZERO)
 x12 = rbind(greater, ONE)
 x13 = lbind(apply, size)
 x14 = lbind(colorfilter, x0)
 x15 = compose(x13, x14)
 x16 = chain(x12, minimum, x15)
 x17 = fork(both, x11, x16)
 x18 = fork(both, x5, x17)
 x19 = extract(x2, x18)
 x20 = other(x2, x19)
 x21 = ofcolor(I, x20)
 x22 = colorfilter(x0, x19)
 x23 = rbind(vmatching, x21)
 x24 = rbind(hmatching, x21)
 x25 = fork(either, x23, x24)
 x26 = extract(x22, x25)
 x27 = other(x22, x26)
 x28 = rbind(gravitate, x26)
 x29 = compose(x28, initset)
 x30 = fork(add, identity, x29)
 x31 = fork(connect, identity, x30)
 x32 = mapply(x31, x21)
 x33 = fill(I, x20, x32)
 x34 = fill(x33, FOUR, x21)
 x35 = ofcolor(I, x19)
 x36 = apply(first, x35)
 x37 = size(x36)
 x38 = apply(last, x35)
 x39 = size(x38)
 x40 = greater(x37, x39)
 x41 = compose(toivec, first)
 x42 = compose(tojvec, last)
 x43 = branch(x40, x41, x42)
 x44 = branch(x40, hfrontier, vfrontier)
 x45 = ulcorner(x26)
 x46 = ulcorner(x27)
 x47 = subtract(x46, x45)
 x48 = x43(x47)
 x49 = shift(x21, x48)
 x50 = mapply(x44, x49)
 x51 = fill(x34, x20, x50)
 x52 = fill(x51, x19, x35)
 return x52
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]