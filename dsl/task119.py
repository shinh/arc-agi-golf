DOWN_LEFT = (1, -1)
F = False
NEG_UNITY = (-1, -1)
ONE = 1
T = True
THREE = 3
UNITY = (1, 1)
UP_RIGHT = (-1, 1)
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def colorfilter(objs,value):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def contained(value,container):
 return value in container
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def equality(a,b):
 return a == b
def extract(container,condition):
 return next(e for e in container if condition(e))
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def greater(a,b):
 return a > b
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
def initset(value):
 return frozenset({value})
def intersection(a,b):
 return a & b
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def matcher(function,target):
 return lambda x: function(x) == target
def maximum(container):
 return max(container, default=0)
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
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
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def outbox(patch):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
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
def verify_task119(I):
 x0 = objects(I, T, F, F)
 x1 = palette(I)
 x2 = compose(maximum, shape)
 x3 = lbind(apply, x2)
 x4 = lbind(colorfilter, x0)
 x5 = chain(maximum, x3, x4)
 x6 = matcher(x5, ONE)
 x7 = extract(x1, x6)
 x8 = lbind(ofcolor, I)
 x9 = compose(backdrop, x8)
 x10 = fork(equality, x8, x9)
 x11 = extract(x1, x10)
 x12 = ofcolor(I, x11)
 x13 = ofcolor(I, x7)
 x14 = rbind(manhattan, x12)
 x15 = compose(x14, initset)
 x16 = argmin(x13, x15)
 x17 = ulcorner(x13)
 x18 = contained(x17, x13)
 x19 = shoot(x16, UNITY)
 x20 = shoot(x16, NEG_UNITY)
 x21 = combine(x19, x20)
 x22 = shoot(x16, UP_RIGHT)
 x23 = shoot(x16, DOWN_LEFT)
 x24 = combine(x22, x23)
 x25 = branch(x18, x21, x24)
 x26 = asindices(I)
 x27 = outbox(x12)
 x28 = intersection(x26, x27)
 x29 = intersection(x28, x25)
 x30 = initset(x16)
 x31 = rbind(manhattan, x30)
 x32 = compose(x31, initset)
 x33 = argmin(x29, x32)
 x34 = height(x12)
 x35 = height(I)
 x36 = equality(x34, x35)
 x37 = leftmost(x13)
 x38 = leftmost(x12)
 x39 = greater(x37, x38)
 x40 = uppermost(x13)
 x41 = uppermost(x12)
 x42 = greater(x40, x41)
 x43 = lbind(shoot, x33)
 x44 = branch(x39, UNITY, NEG_UNITY)
 x45 = branch(x39, UP_RIGHT, DOWN_LEFT)
 x46 = branch(x42, UNITY, NEG_UNITY)
 x47 = branch(x42, DOWN_LEFT, UP_RIGHT)
 x48 = branch(x36, x44, x46)
 x49 = branch(x36, x45, x47)
 x50 = x43(x48)
 x51 = x43(x49)
 x52 = combine(x50, x51)
 x53 = difference(x52, x13)
 x54 = fill(I, THREE, x53)
 return x54
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]