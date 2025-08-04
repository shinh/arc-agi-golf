def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(
 patch
):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
T = True
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def delta(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 return backdrop(patch) - toindices(patch)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def lbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def maximum(
 container
):
 return max(container, default=0)
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def valmax(
 container,
 compfunc
):
 return compfunc(max(container, key=compfunc, default=0))
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
ONE = 1
def paint(
 grid,
 obj
):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def equality(
 a,
 b
):
 return a == b
def last(
 container
):
 return max(enumerate(container))[1]
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def add(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def ineighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(
 loc
):
 return dneighbors(loc) | ineighbors(loc)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def objects(
 grid,
 univalued,
 diagonal,
 without_bg
):
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def width(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def color(
 obj
):
 return next(iter(obj))[0]
def manhattan(
 a,
 b
):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def shift(
 patch,
 directions
):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
F = False
def verify_task122(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = valmax(x0, x1)
 x3 = matcher(x1, x2)
 x4 = sfilter(x0, x3)
 x5 = argmax(x4, size)
 x6 = color(x5)
 x7 = remove(x5, x0)
 x8 = objects(I, T, F, F)
 x9 = lbind(colorfilter, x8)
 x10 = chain(size, x9, color)
 x11 = argmin(x7, x10)
 x12 = other(x7, x11)
 x13 = color(x12)
 x14 = colorfilter(x8, x13)
 x15 = apply(leftmost, x14)
 x16 = size(x15)
 x17 = equality(ONE, x16)
 x18 = apply(uppermost, x14)
 x19 = size(x18)
 x20 = equality(ONE, x19)
 x21 = fork(add, first, last)
 x22 = compose(x21, ulcorner)
 x23 = argmin(x14, x22)
 x24 = remove(x23, x14)
 x25 = lbind(manhattan, x23)
 x26 = argmin(x24, x25)
 x27 = lowermost(x26)
 x28 = lowermost(x23)
 x29 = subtract(x27, x28)
 x30 = uppermost(x26)
 x31 = uppermost(x23)
 x32 = subtract(x30, x31)
 x33 = astuple(x29, x32)
 x34 = maximum(x33)
 x35 = branch(x20, ZERO, x34)
 x36 = rightmost(x26)
 x37 = rightmost(x23)
 x38 = subtract(x36, x37)
 x39 = leftmost(x26)
 x40 = leftmost(x23)
 x41 = subtract(x39, x40)
 x42 = astuple(x38, x41)
 x43 = maximum(x42)
 x44 = branch(x17, ZERO, x43)
 x45 = astuple(x35, x44)
 x46 = shift(x11, x45)
 x47 = delta(x46)
 x48 = hmirror(x46)
 x49 = ulcorner(x47)
 x50 = delta(x48)
 x51 = ulcorner(x50)
 x52 = subtract(x49, x51)
 x53 = shift(x48, x52)
 x54 = combine(x46, x53)
 x55 = vmirror(x54)
 x56 = ulcorner(x47)
 x57 = delta(x55)
 x58 = ulcorner(x57)
 x59 = subtract(x56, x58)
 x60 = shift(x55, x59)
 x61 = combine(x60, x54)
 x62 = color(x11)
 x63 = replace(I, x62, x6)
 x64 = paint(x63, x61)
 return x64
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]