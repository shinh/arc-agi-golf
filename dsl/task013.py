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
T = True
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def tojvec(
 j
):
 return (0, j)
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
TEN = 10
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
def portrait(
 piece
):
 return height(piece) > width(piece)
def vfrontier(
 location
):
 return frozenset((i, location[1]) for i in range(30))
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def identity(
 x
):
 return x
def color(
 obj
):
 return next(iter(obj))[0]
THREE = 3
F = False
def verify_task013(I):
 x0 = portrait(I)
 x1 = branch(x0, dmirror, identity)
 x2 = x1(I)
 x3 = objects(x2, T, F, T)
 x4 = argmin(x3, leftmost)
 x5 = argmax(x3, leftmost)
 x6 = color(x4)
 x7 = color(x5)
 x8 = leftmost(x4)
 x9 = leftmost(x5)
 x10 = subtract(x9, x8)
 x11 = double(x10)
 x12 = multiply(THREE, TEN)
 x13 = interval(x8, x12, x11)
 x14 = interval(x9, x12, x11)
 x15 = compose(vfrontier, tojvec)
 x16 = mapply(x15, x13)
 x17 = mapply(x15, x14)
 x18 = recolor(x6, x16)
 x19 = recolor(x7, x17)
 x20 = combine(x18, x19)
 x21 = paint(x2, x20)
 x22 = x1(x21)
 return x22
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]