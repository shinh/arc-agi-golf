F = False
ONE = 1
T = True
THREE = 3
TWO = 2
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
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def both(
 a,
 b
):
 return a and b
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
def equality(
 a,
 b
):
 return a == b
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def verify_task226(I):
 x0 = asindices(I)
 x1 = corners(x0)
 x2 = toobject(x1, I)
 x3 = mostcolor(x2)
 x4 = objects(I, T, T, F)
 x5 = colorfilter(x4, x3)
 x6 = fork(add, leftmost, uppermost)
 x7 = argmin(x5, x6)
 x8 = argmax(x5, x6)
 x9 = lbind(sfilter, x5)
 x10 = rbind(compose, leftmost)
 x11 = chain(size, x9, x10)
 x12 = lbind(sfilter, x5)
 x13 = rbind(compose, uppermost)
 x14 = chain(size, x12, x13)
 x15 = lbind(lbind, greater)
 x16 = chain(x11, x15, leftmost)
 x17 = lbind(rbind, greater)
 x18 = chain(x11, x17, leftmost)
 x19 = lbind(lbind, greater)
 x20 = chain(x14, x19, uppermost)
 x21 = lbind(rbind, greater)
 x22 = chain(x14, x21, uppermost)
 x23 = fork(equality, x16, x18)
 x24 = fork(equality, x20, x22)
 x25 = fork(both, x23, x24)
 x26 = extract(x5, x25)
 x27 = fill(I, ONE, x7)
 x28 = fill(x27, THREE, x8)
 x29 = fill(x28, TWO, x26)
 return x29
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]