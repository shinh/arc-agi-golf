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
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
T = True
def toivec(
 i
):
 return (i, 0)
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
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def first(
 container
):
 return next(iter(container))
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def portrait(
 piece
):
 return height(piece) > width(piece)
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
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
FOUR = 4
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
def hconcat(
 a,
 b
):
 return tuple(i + j for i, j in zip(a, b))
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
F = False
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task214(I):
 x0 = portrait(I)
 x1 = branch(x0, identity, rot90)
 x2 = branch(x0, identity, rot270)
 x3 = x1(I)
 x4 = width(x3)
 x5 = toivec(x4)
 x6 = index(x3, x5)
 x7 = shape(x3)
 x8 = canvas(x6, x7)
 x9 = hconcat(x3, x8)
 x10 = objects(x9, F, T, T)
 x11 = argmax(x10, numcolors)
 x12 = subgrid(x11, x3)
 x13 = interval(ONE, FOUR, ONE)
 x14 = lbind(power, rot90)
 x15 = lbind(power, rot270)
 x16 = rbind(rapply, x12)
 x17 = compose(initset, x14)
 x18 = chain(first, x16, x17)
 x19 = rbind(rapply, x12)
 x20 = compose(initset, x15)
 x21 = chain(first, x19, x20)
 x22 = compose(asobject, x18)
 x23 = uppermost(x11)
 x24 = lbind(add, x23)
 x25 = height(x11)
 x26 = increment(x25)
 x27 = lbind(multiply, x26)
 x28 = chain(toivec, x24, x27)
 x29 = fork(shift, x22, x28)
 x30 = compose(asobject, x21)
 x31 = uppermost(x11)
 x32 = lbind(subtract, x31)
 x33 = height(x11)
 x34 = increment(x33)
 x35 = lbind(multiply, x34)
 x36 = chain(toivec, x32, x35)
 x37 = fork(shift, x30, x36)
 x38 = fork(combine, x29, x37)
 x39 = mapply(x38, x13)
 x40 = paint(x3, x39)
 x41 = x2(x40)
 return x41
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]