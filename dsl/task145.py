def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
T = True
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def valmax(
 container,
 compfunc
):
 return compfunc(max(container, key=compfunc, default=0))
ONE = 1
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
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
def size(
 container
):
 return len(container)
def sizefilter(
 container,
 n
):
 return frozenset(item for item in container if len(item) == n)
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def valmin(
 container,
 compfunc
):
 return compfunc(min(container, key=compfunc, default=0))
F = False
EIGHT = 8
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
def verify_task145(I):
 x0 = objects(I, T, F, F)
 x1 = asindices(I)
 x2 = corners(x1)
 x3 = toobject(x2, I)
 x4 = mostcolor(x3)
 x5 = colorfilter(x0, x4)
 x6 = valmax(x5, size)
 x7 = valmin(x5, size)
 x8 = sizefilter(x5, x6)
 x9 = sizefilter(x5, x7)
 x10 = merge(x8)
 x11 = fill(I, ONE, x10)
 x12 = merge(x9)
 x13 = fill(x11, EIGHT, x12)
 return x13
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]