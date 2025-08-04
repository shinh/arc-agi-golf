def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(
 element
):
 return len(palette(element))
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def first(
 container
):
 return next(iter(container))
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def size(
 container
):
 return len(container)
def positive(
 x
):
 return x > 0
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
def contained(
 value,
 container
):
 return value in container
THREE = 3
F = False
TWO = 2
def verify_task089(I):
 x0 = ofcolor(I, THREE)
 x1 = ofcolor(I, TWO)
 x2 = matcher(first, THREE)
 x3 = matcher(first, TWO)
 x4 = rbind(objects, T)
 x5 = rbind(x4, T)
 x6 = rbind(x5, F)
 x7 = lbind(contained, THREE)
 x8 = compose(x7, palette)
 x9 = lbind(contained, TWO)
 x10 = compose(x9, palette)
 x11 = rbind(sfilter, x8)
 x12 = compose(x11, x6)
 x13 = rbind(sfilter, x10)
 x14 = compose(x13, x6)
 x15 = rbind(argmax, numcolors)
 x16 = chain(normalize, x15, x12)
 x17 = rbind(argmax, numcolors)
 x18 = compose(x17, x14)
 x19 = chain(normalize, vmirror, x18)
 x20 = rbind(sfilter, x2)
 x21 = chain(ulcorner, x20, x16)
 x22 = rbind(sfilter, x3)
 x23 = chain(ulcorner, x22, x19)
 x24 = rbind(sfilter, x3)
 x25 = chain(center, x24, x18)
 x26 = lbind(lbind, shift)
 x27 = compose(x26, x16)
 x28 = lbind(lbind, shift)
 x29 = compose(x28, x19)
 x30 = rbind(apply, x0)
 x31 = lbind(lbind, add)
 x32 = compose(invert, x21)
 x33 = chain(x30, x31, x32)
 x34 = rbind(remove, x1)
 x35 = compose(x34, x25)
 x36 = lbind(lbind, add)
 x37 = chain(x36, invert, x23)
 x38 = fork(apply, x37, x35)
 x39 = fork(mapply, x27, x33)
 x40 = fork(mapply, x29, x38)
 x41 = fork(paint, identity, x39)
 x42 = fork(paint, identity, x40)
 x43 = size(x0)
 x44 = positive(x43)
 x45 = size(x1)
 x46 = positive(x45)
 x47 = branch(x44, x41, identity)
 x48 = branch(x46, x42, identity)
 x49 = compose(x47, x48)
 x50 = x49(I)
 return x50
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]