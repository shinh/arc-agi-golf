DOWN = (1, 0)
FOUR = 4
ONE = 1
RIGHT = (0, 1)
SIX = 6
THREE = 3
TWO = 2
UNITY = (1, 1)
ZERO_BY_TWO = (0, 2)
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
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
F = False
T = True
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
def occurrences(grid,obj):
 occurrences = set()
 normed = normalize(obj)
 h, w = len(grid), len(grid[0])
 for i in range(h):
  for j in range(w):
   occurs = True
   for v, (a, b) in shift(normed, (i, j)):
    if 0 <= a < h and 0 <= b < w:
     if grid[a][b] != v:
      occurs = False
      break
    else:
     occurs = False
     break
   if occurs:
    occurrences.add((i, j))
 return frozenset(occurrences)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def lowermost(patch):
 return max(i for i, j in toindices(patch))
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
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def power(function,n):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
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
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def shape(piece):
 return (height(piece), width(piece))
def trim(grid):
 return tuple(r[1:-1] for r in grid[1:-1])
def verify_task255(I):
 x0 = mostcolor(I)
 x1 = shape(I)
 x2 = add(TWO, x1)
 x3 = canvas(x0, x2)
 x4 = asobject(I)
 x5 = shift(x4, UNITY)
 x6 = paint(x3, x5)
 x7 = double(SIX)
 x8 = astuple(ONE, x7)
 x9 = connect(UNITY, x8)
 x10 = outbox(x9)
 x11 = backdrop(x10)
 x12 = recolor(x0, x11)
 x13 = recolor(THREE, x9)
 x14 = lbind(shift, x13)
 x15 = lbind(mapply, x14)
 x16 = rbind(occurrences, x12)
 x17 = compose(x15, x16)
 x18 = fork(paint, identity, x17)
 x19 = x18(x6)
 x20 = ofcolor(x19, THREE)
 x21 = dmirror(x6)
 x22 = x18(x21)
 x23 = dmirror(x22)
 x24 = ofcolor(x23, THREE)
 x25 = combine(x20, x24)
 x26 = fill(x6, THREE, x25)
 x27 = astuple(TWO, ONE)
 x28 = dneighbors(UNITY)
 x29 = remove(x27, x28)
 x30 = recolor(x0, x29)
 x31 = initset(UNITY)
 x32 = recolor(THREE, x31)
 x33 = combine(x30, x32)
 x34 = recolor(x0, x33)
 x35 = astuple(ONE, THREE)
 x36 = initset(x35)
 x37 = insert(ZERO_BY_TWO, x36)
 x38 = insert(RIGHT, x37)
 x39 = insert(DOWN, x38)
 x40 = recolor(x0, x39)
 x41 = astuple(ONE, TWO)
 x42 = initset(x41)
 x43 = insert(UNITY, x42)
 x44 = recolor(THREE, x43)
 x45 = combine(x40, x44)
 x46 = recolor(x0, x45)
 x47 = lbind(shift, x34)
 x48 = lbind(mapply, x47)
 x49 = rbind(occurrences, x33)
 x50 = compose(x48, x49)
 x51 = fork(paint, identity, x50)
 x52 = lbind(shift, x46)
 x53 = lbind(mapply, x52)
 x54 = rbind(occurrences, x45)
 x55 = compose(x53, x54)
 x56 = fork(paint, identity, x55)
 x57 = compose(x51, x56)
 x58 = compose(rot90, x57)
 x59 = power(x58, FOUR)
 x60 = power(x59, TWO)
 x61 = asindices(x26)
 x62 = box(x61)
 x63 = fill(x26, THREE, x62)
 x64 = x60(x63)
 x65 = trim(x64)
 return x65
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]