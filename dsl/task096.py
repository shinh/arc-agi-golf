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
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
T = True
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def pair(
 a,
 b
):
 return tuple(zip(a, b))
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
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
def maximum(
 container
):
 return max(container, default=0)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
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
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def papply(
 function,
 a,
 b
):
 return tuple(function(i, j) for i, j in zip(a, b))
def mpapply(
 function,
 a,
 b
):
 return merge(papply(function, a, b))
def valmax(
 container,
 compfunc
):
 return compfunc(max(container, key=compfunc, default=0))
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
def initset(
 value
):
 return frozenset({value})
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
ZERO = 0
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
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
RIGHT = (0, 1)
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
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
def identity(
 x
):
 return x
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def color(
 obj
):
 return next(iter(obj))[0]
def contained(
 value,
 container
):
 return value in container
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
DOWN = (1, 0)
F = False
def verify_task096(I):
 x0 = mostcolor(I)
 x1 = fgpartition(I)
 x2 = objects(I, T, F, T)
 x3 = rbind(valmax, width)
 x4 = lbind(colorfilter, x2)
 x5 = chain(x3, x4, color)
 x6 = compose(maximum, shape)
 x7 = fork(add, x6, x5)
 x8 = compose(invert, x7)
 x9 = order(x1, x8)
 x10 = rbind(add, DOWN)
 x11 = compose(x10, ulcorner)
 x12 = fork(contained, x11, toindices)
 x13 = rbind(add, RIGHT)
 x14 = compose(x13, ulcorner)
 x15 = fork(contained, x14, toindices)
 x16 = fork(add, x12, x15)
 x17 = rbind(argmax, x16)
 x18 = compose(initset, identity)
 x19 = fork(insert, vmirror, x18)
 x20 = fork(insert, cmirror, x19)
 x21 = fork(insert, hmirror, x20)
 x22 = compose(x17, x21)
 x23 = apply(x22, x9)
 x24 = size(x1)
 x25 = apply(size, x1)
 x26 = contained(ONE, x25)
 x27 = increment(x24)
 x28 = branch(x26, x24, x27)
 x29 = double(x28)
 x30 = decrement(x29)
 x31 = apply(normalize, x23)
 x32 = interval(ZERO, x28, ONE)
 x33 = pair(x32, x32)
 x34 = mpapply(shift, x31, x33)
 x35 = astuple(x30, x30)
 x36 = canvas(x0, x35)
 x37 = paint(x36, x34)
 x38 = rot90(x37)
 x39 = paint(x38, x34)
 x40 = rot90(x39)
 x41 = paint(x40, x34)
 x42 = rot90(x41)
 x43 = paint(x42, x34)
 return x43
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]