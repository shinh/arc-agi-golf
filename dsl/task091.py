DOWN = (1, 0)
F = False
LEFT = (0, -1)
RIGHT = (0, 1)
T = True
TWO = 2
UP = (-1, 0)
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
def both(
 a,
 b
):
 return a and b
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
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def either(
 a,
 b
):
 return a or b
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
def first(
 container
):
 return next(iter(container))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def shape(
 piece
):
 return (height(piece), width(piece))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def vline(
 patch
):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task091(I):
 x0 = partition(I)
 x1 = objects(I, T, F, F)
 x2 = compose(double, height)
 x3 = fork(equality, x2, size)
 x4 = compose(double, width)
 x5 = fork(equality, x4, size)
 x6 = fork(either, x3, x5)
 x7 = rbind(equality, TWO)
 x8 = lbind(colorfilter, x1)
 x9 = rbind(sfilter, vline)
 x10 = rbind(sfilter, hline)
 x11 = chain(x9, x8, color)
 x12 = chain(x7, size, x11)
 x13 = chain(x10, x8, color)
 x14 = chain(x7, size, x13)
 x15 = fork(either, x12, x14)
 x16 = fork(both, x6, x15)
 x17 = extract(x0, x16)
 x18 = color(x17)
 x19 = colorfilter(x1, x18)
 x20 = first(x19)
 x21 = vline(x20)
 x22 = ulcorner(x17)
 x23 = lrcorner(x17)
 x24 = branch(x21, UP, LEFT)
 x25 = add(x22, x24)
 x26 = branch(x21, DOWN, RIGHT)
 x27 = add(x23, x26)
 x28 = initset(x27)
 x29 = insert(x25, x28)
 x30 = subgrid(x29, I)
 return x30
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]