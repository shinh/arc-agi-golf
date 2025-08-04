F = False
ORIGIN = (0, 0)
RIGHT = (0, 1)
T = True
ZERO_BY_TWO = (0, 2)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(
 a,
 b
):
 return (a, b)
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def color(
 obj
):
 return next(iter(obj))[0]
def combine(
 a,
 b
):
 return type(a)((*a, *b))
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
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
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
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def occurrences(
 grid,
 obj
):
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
def shape(
 piece
):
 return (height(piece), width(piece))
def size(
 container
):
 return len(container)
def verify_task222(I):
 x0 = shape(I)
 x1 = asindices(I)
 x2 = objects(I, T, F, T)
 x3 = argmax(x2, size)
 x4 = mostcolor(x3)
 x5 = mostcolor(I)
 x6 = canvas(x5, x0)
 x7 = paint(x6, x3)
 x8 = mostcolor(I)
 x9 = color(x3)
 x10 = astuple(x8, ORIGIN)
 x11 = astuple(x9, RIGHT)
 x12 = astuple(x8, ZERO_BY_TWO)
 x13 = initset(x12)
 x14 = insert(x11, x13)
 x15 = insert(x10, x14)
 x16 = dmirror(x15)
 x17 = toindices(x15)
 x18 = lbind(shift, x17)
 x19 = occurrences(x7, x15)
 x20 = mapply(x18, x19)
 x21 = toindices(x16)
 x22 = lbind(shift, x21)
 x23 = occurrences(x7, x16)
 x24 = mapply(x22, x23)
 x25 = combine(x20, x24)
 x26 = fill(x7, x8, x25)
 return x26
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]