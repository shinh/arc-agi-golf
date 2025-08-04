F = False
ONE = 1
ORIGIN = (0, 0)
RIGHT = (0, 1)
T = True
TWO = 2
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def astuple(
 a,
 b
):
 return (a, b)
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
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def contained(
 value,
 container
):
 return value in container
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
def fill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def cover(
 grid,
 patch
):
 return fill(grid, mostcolor(grid), toindices(patch))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def identity(
 x
):
 return x
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def last(
 container
):
 return max(enumerate(container))[1]
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def manhattan(
 a,
 b
):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def ineighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(
 loc
):
 return dneighbors(loc) | ineighbors(loc)
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def rbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
def size(
 container
):
 return len(container)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
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
def verify_task046(I):
 x0 = objects(I, F, F, T)
 x1 = order(x0, leftmost)
 x2 = astuple(ONE, TWO)
 x3 = rbind(contained, x2)
 x4 = lbind(compose, x3)
 x5 = lbind(rbind, colorcount)
 x6 = compose(x4, x5)
 x7 = lbind(sfilter, x0)
 x8 = chain(size, x7, x6)
 x9 = size(x0)
 x10 = matcher(x8, x9)
 x11 = palette(I)
 x12 = sfilter(x11, x10)
 x13 = lbind(colorcount, I)
 x14 = argmin(x12, x13)
 x15 = matcher(first, x14)
 x16 = rbind(extract, x15)
 x17 = compose(x16, first)
 x18 = fork(remove, x17, first)
 x19 = rbind(compose, initset)
 x20 = lbind(rbind, manhattan)
 x21 = compose(initset, x17)
 x22 = chain(x19, x20, x21)
 x23 = fork(argmin, x18, x22)
 x24 = compose(last, x17)
 x25 = compose(first, x23)
 x26 = fork(astuple, x25, x24)
 x27 = fork(insert, x26, x18)
 x28 = compose(last, last)
 x29 = rbind(argmin, x28)
 x30 = rbind(sfilter, x15)
 x31 = compose(first, last)
 x32 = chain(x29, x30, x31)
 x33 = compose(flip, x15)
 x34 = rbind(sfilter, x33)
 x35 = compose(first, last)
 x36 = fork(remove, x32, x35)
 x37 = compose(x34, x36)
 x38 = rbind(compose, initset)
 x39 = lbind(rbind, manhattan)
 x40 = compose(initset, x32)
 x41 = chain(x38, x39, x40)
 x42 = fork(argmin, x37, x41)
 x43 = compose(first, x42)
 x44 = compose(last, x32)
 x45 = fork(astuple, x43, x44)
 x46 = compose(first, last)
 x47 = fork(remove, x32, x46)
 x48 = fork(insert, x45, x47)
 x49 = rbind(shift, RIGHT)
 x50 = compose(last, x32)
 x51 = fork(subtract, x24, x50)
 x52 = fork(shift, x48, x51)
 x53 = compose(x49, x52)
 x54 = fork(combine, x27, x53)
 x55 = compose(first, last)
 x56 = fork(remove, x55, last)
 x57 = fork(astuple, x54, x56)
 x58 = size(x0)
 x59 = decrement(x58)
 x60 = power(x57, x59)
 x61 = first(x1)
 x62 = remove(x61, x1)
 x63 = astuple(x61, x62)
 x64 = x60(x63)
 x65 = first(x64)
 x66 = merge(x0)
 x67 = cover(I, x66)
 x68 = paint(x67, x65)
 x69 = height(I)
 x70 = width(x65)
 x71 = astuple(x69, x70)
 x72 = crop(x68, ORIGIN, x71)
 x73 = ofcolor(x72, x14)
 x74 = mostcolor(I)
 x75 = palette(x72)
 x76 = contained(x14, x75)
 x77 = matcher(first, x74)
 x78 = compose(flip, x77)
 x79 = rbind(sfilter, x78)
 x80 = mapply(dneighbors, x73)
 x81 = lbind(toobject, x80)
 x82 = compose(x79, x81)
 x83 = rbind(recolor, x73)
 x84 = chain(x83, mostcolor, x82)
 x85 = fork(paint, identity, x84)
 x86 = branch(x76, x85, identity)
 x87 = x86(x72)
 return x87
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]