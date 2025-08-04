F = False
FIVE = 5
FOUR = 4
ONE = 1
SIX = 6
T = True
TEN = 10
THREE = 3
TWO = 2
UNITY = (1, 1)
ZERO = 0
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
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def divide(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def downscale(
 grid,
 factor
):
 h, w = len(grid), len(grid[0])
 downscaled_grid = tuple()
 for i in range(h):
  downscaled_row = tuple()
  for j in range(w):
   if j % factor == 0:
    downscaled_row = downscaled_row + (grid[i][j],)
  downscaled_grid = downscaled_grid + (downscaled_row, )
 h = len(downscaled_grid)
 downscaled_grid2 = tuple()
 for i in range(h):
  if i % factor == 0:
   downscaled_grid2 = downscaled_grid2 + (downscaled_grid[i],)
 return downscaled_grid2
def equality(
 a,
 b
):
 return a == b
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
def identity(
 x
):
 return x
def initset(
 value
):
 return frozenset({value})
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def last(
 container
):
 return max(enumerate(container))[1]
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
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def positive(
 x
):
 return x > 0
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
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
def valmax(
 container,
 compfunc
):
 return compfunc(max(container, key=compfunc, default=0))
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
def verify_task056(I):
 x0 = lbind(apply, last)
 x1 = compose(positive, first)
 x2 = lbind(interval, ZERO)
 x3 = rbind(x2, ONE)
 x4 = rbind(sfilter, x1)
 x5 = compose(x3, size)
 x6 = fork(pair, x5, identity)
 x7 = chain(x0, x4, x6)
 x8 = rbind(branch, identity)
 x9 = rbind(x8, x7)
 x10 = chain(size, dedupe, first)
 x11 = lbind(equality, ONE)
 x12 = chain(x9, x11, x10)
 x13 = compose(initset, x12)
 x14 = fork(rapply, x13, identity)
 x15 = compose(first, x14)
 x16 = rbind(branch, identity)
 x17 = rbind(x16, x15)
 x18 = chain(x17, positive, size)
 x19 = compose(initset, x18)
 x20 = fork(rapply, x19, identity)
 x21 = compose(first, x20)
 x22 = multiply(TEN, THREE)
 x23 = power(x21, x22)
 x24 = compose(rot90, x23)
 x25 = power(x24, FOUR)
 x26 = x25(I)
 x27 = width(x26)
 x28 = divide(x27, THREE)
 x29 = downscale(x26, x28)
 x30 = objects(x29, T, F, F)
 x31 = valmax(x30, size)
 x32 = equality(x31, ONE)
 x33 = equality(x31, FOUR)
 x34 = equality(x31, FIVE)
 x35 = branch(x32, TWO, ONE)
 x36 = branch(x33, THREE, x35)
 x37 = branch(x34, SIX, x36)
 x38 = canvas(x37, UNITY)
 return x38
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]