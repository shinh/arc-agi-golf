F = False
FOUR = 4
ONE = 1
ORIGIN = (0, 0)
SIX = 6
T = True
THREE = 3
TWO = 2
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def bordering(
 patch,
 grid
):
 return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1
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
def flip(
 b
):
 return not b
def hmatching(
 a,
 b
):
 return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def vmatching(
 a,
 b
):
 return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0
def verify_task055(I):
 x0 = objects(I, T, F, F)
 x1 = index(I, ORIGIN)
 x2 = colorfilter(x0, x1)
 x3 = apply(toindices, x2)
 x4 = rbind(bordering, I)
 x5 = compose(flip, x4)
 x6 = extract(x3, x5)
 x7 = remove(x6, x3)
 x8 = lbind(vmatching, x6)
 x9 = lbind(hmatching, x6)
 x10 = sfilter(x7, x8)
 x11 = sfilter(x7, x9)
 x12 = argmin(x10, uppermost)
 x13 = argmax(x10, uppermost)
 x14 = argmin(x11, leftmost)
 x15 = argmax(x11, leftmost)
 x16 = fill(I, SIX, x6)
 x17 = fill(x16, TWO, x12)
 x18 = fill(x17, ONE, x13)
 x19 = fill(x18, FOUR, x14)
 x20 = fill(x19, THREE, x15)
 return x20
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]