def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
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
UNITY = (1, 1)
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
ZERO = 0
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
ORIGIN = (0, 0)
FOUR = 4
def connect(
 a,
 b
):
 ai, aj = a
 bi, bj = b
 si = min(ai, bi)
 ei = max(ai, bi) + 1
 sj = min(aj, bj)
 ej = max(aj, bj) + 1
 if ai == bi:
  return frozenset((ai, j) for j in range(sj, ej))
 elif aj == bj:
  return frozenset((i, aj) for i in range(si, ei))
 elif bi - ai == bj - aj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
 elif bi - ai == aj - bj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
 return frozenset()
def shoot(
 start,
 direction
):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def identity(
 x
):
 return x
def contained(
 value,
 container
):
 return value in container
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
def verify_task252(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = compose(increment, double)
 x3 = shoot(ORIGIN, UNITY)
 x4 = apply(x2, x3)
 x5 = order(x4, identity)
 x6 = lbind(contained, ZERO)
 x7 = sfilter(x1, x6)
 x8 = lbind(shift, x5)
 x9 = mapply(x8, x7)
 x10 = fill(I, FOUR, x9)
 return x10
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]