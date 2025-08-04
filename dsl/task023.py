EIGHT = 8
FIVE = 5
FOUR = 4
ONE = 1
ORIGIN = (0, 0)
THREE = 3
THREE_BY_THREE = (3, 3)
TWO = 2
TWO_BY_TWO = (2, 2)
UNITY = (1, 1)
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
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
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
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
def leastcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
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
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
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
def verify_task023(I):
 x0 = mostcolor(I)
 x1 = leastcolor(I)
 x2 = shape(I)
 x3 = add(TWO, x2)
 x4 = canvas(x0, x3)
 x5 = asobject(I)
 x6 = shift(x5, UNITY)
 x7 = paint(x4, x6)
 x8 = astuple(TWO, ONE)
 x9 = dneighbors(UNITY)
 x10 = remove(x8, x9)
 x11 = recolor(x0, x10)
 x12 = initset(UNITY)
 x13 = recolor(x1, x12)
 x14 = combine(x11, x13)
 x15 = astuple(THREE, ONE)
 x16 = connect(UNITY, x15)
 x17 = recolor(TWO, x16)
 x18 = initset(TWO_BY_TWO)
 x19 = insert(UNITY, x18)
 x20 = backdrop(x19)
 x21 = astuple(TWO, THREE)
 x22 = astuple(THREE, TWO)
 x23 = initset(x22)
 x24 = insert(x21, x23)
 x25 = insert(THREE_BY_THREE, x24)
 x26 = recolor(x1, x20)
 x27 = outbox(x20)
 x28 = difference(x27, x25)
 x29 = recolor(x0, x28)
 x30 = combine(x26, x29)
 x31 = recolor(EIGHT, x20)
 x32 = lbind(lbind, shift)
 x33 = compose(x32, last)
 x34 = lbind(fork, paint)
 x35 = lbind(x34, identity)
 x36 = lbind(lbind, mapply)
 x37 = compose(x36, x33)
 x38 = lbind(rbind, occurrences)
 x39 = compose(x38, first)
 x40 = fork(compose, x37, x39)
 x41 = compose(x35, x40)
 x42 = astuple(x14, x17)
 x43 = x41(x42)
 x44 = compose(rot90, x43)
 x45 = power(x44, FOUR)
 x46 = astuple(x30, x31)
 x47 = x41(x46)
 x48 = compose(rot90, x47)
 x49 = power(x48, FOUR)
 x50 = compose(x45, x49)
 x51 = initset(ORIGIN)
 x52 = difference(x51, x51)
 x53 = lbind(recolor, TWO)
 x54 = rbind(ofcolor, TWO)
 x55 = compose(x53, x54)
 x56 = lbind(recolor, EIGHT)
 x57 = rbind(ofcolor, EIGHT)
 x58 = compose(x56, x57)
 x59 = fork(combine, x55, x58)
 x60 = lbind(recolor, x0)
 x61 = compose(x60, x59)
 x62 = fork(paint, identity, x61)
 x63 = chain(x62, x50, first)
 x64 = chain(x59, x50, first)
 x65 = fork(combine, last, x64)
 x66 = fork(astuple, x63, x65)
 x67 = astuple(x7, x52)
 x68 = power(x66, FIVE)
 x69 = x68(x67)
 x70 = first(x69)
 x71 = last(x69)
 x72 = paint(x70, x71)
 x73 = trim(x72)
 return x73
def p(g):
 return [list(r)for r in verify_task023(tuple(tuple(r) for r in g))]