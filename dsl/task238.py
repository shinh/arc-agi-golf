F = False
T = True
UNITY = (1, 1)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def color(
 obj
):
 return next(iter(obj))[0]
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def equality(
 a,
 b
):
 return a == b
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def greater(
 a,
 b
):
 return a > b
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
def initset(
 value
):
 return frozenset({value})
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
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
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def outbox(
 patch
):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
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
def size(
 container
):
 return len(container)
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def width(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def valmin(
 container,
 compfunc
):
 return compfunc(min(container, key=compfunc, default=0))
def verify_task238(I):
 x0 = objects(I, T, F, F)
 x1 = fork(multiply, height, width)
 x2 = fork(equality, size, x1)
 x3 = sfilter(x0, x2)
 x4 = mostcolor(I)
 x5 = colorfilter(x3, x4)
 x6 = argmax(x5, size)
 x7 = outbox(x6)
 x8 = backdrop(x7)
 x9 = subgrid(x8, I)
 x10 = cover(I, x8)
 x11 = fgpartition(x10)
 x12 = merge(x11)
 x13 = normalize(x12)
 x14 = shift(x13, UNITY)
 x15 = paint(x9, x14)
 x16 = toindices(x14)
 x17 = fgpartition(x9)
 x18 = rbind(remove, x17)
 x19 = lbind(lbind, manhattan)
 x20 = compose(x19, initset)
 x21 = lbind(fork, greater)
 x22 = lbind(sfilter, x16)
 x23 = rbind(compose, x20)
 x24 = lbind(lbind, valmin)
 x25 = chain(x23, x24, x18)
 x26 = rbind(compose, initset)
 x27 = lbind(rbind, manhattan)
 x28 = compose(x26, x27)
 x29 = fork(x21, x25, x28)
 x30 = compose(x22, x29)
 x31 = fork(recolor, color, x30)
 x32 = mapply(x31, x17)
 x33 = paint(x15, x32)
 return x33
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]