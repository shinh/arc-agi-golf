F = False
ONE = 1
T = True
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
def color(
 obj
):
 return next(iter(obj))[0]
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
def equality(
 a,
 b
):
 return a == b
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def maximum(
 container
):
 return max(container, default=0)
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
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
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
def shape(
 piece
):
 return (height(piece), width(piece))
def verify_task298(I):
 x0 = objects(I, T, F, F)
 x1 = compose(maximum, shape)
 x2 = order(x0, x1)
 x3 = first(x2)
 x4 = last(x2)
 x5 = color(x3)
 x6 = color(x4)
 x7 = equality(x5, x6)
 x8 = combine(x3, x4)
 x9 = repeat(x8, ONE)
 x10 = remove(x3, x2)
 x11 = remove(x4, x10)
 x12 = combine(x9, x11)
 x13 = branch(x7, x12, x2)
 x14 = apply(color, x13)
 x15 = last(x13)
 x16 = remove(x15, x13)
 x17 = repeat(x15, ONE)
 x18 = combine(x17, x16)
 x19 = mpapply(recolor, x14, x18)
 x20 = paint(I, x19)
 return x20
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]