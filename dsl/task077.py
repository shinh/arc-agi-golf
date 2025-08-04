def sign(
 x
):
 if isinstance(x, int):
  return 0 if x == 0 else (1 if x > 0 else -1)
 return (
  0 if x[0] == 0 else (1 if x[0] > 0 else -1),
  0 if x[1] == 0 else (1 if x[1] > 0 else -1)
 )
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
def maximum(
 container
):
 return max(container, default=0)
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
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
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
def astuple(
 a,
 b
):
 return (a, b)
FOUR = 4
def greater(
 a,
 b
):
 return a > b
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
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
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
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
THREE = 3
TWO = 2
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
def verify_task077(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = fork(subtract, first, last)
 x3 = fork(multiply, sign, identity)
 x4 = compose(x3, x2)
 x5 = lbind(greater, THREE)
 x6 = chain(x5, maximum, x4)
 x7 = lbind(lbind, astuple)
 x8 = rbind(chain, x7)
 x9 = lbind(compose, x6)
 x10 = rbind(x8, x9)
 x11 = lbind(lbind, sfilter)
 x12 = compose(x10, x11)
 x13 = lbind(mapply, backdrop)
 x14 = fork(apply, x12, identity)
 x15 = compose(x13, x14)
 x16 = power(x15, TWO)
 x17 = x16(x1)
 x18 = fill(I, FOUR, x17)
 x19 = fill(x18, x0, x1)
 return x19
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]