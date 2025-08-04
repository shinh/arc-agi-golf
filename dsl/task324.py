DOWN_LEFT = (1, -1)
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
NEG_UNITY = (-1, -1)
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
def size(
 container
):
 return len(container)
def intersection(
 a,
 b
):
 return a & b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def totuple(
 container
):
 return tuple(container)
UP_RIGHT = (-1, 1)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def verify_task324(I):
 x0 = lbind(ofcolor, I)
 x1 = lbind(mapply, neighbors)
 x2 = compose(x1, x0)
 x3 = fork(intersection, x0, x2)
 x4 = compose(size, x3)
 x5 = palette(I)
 x6 = matcher(x4, ZERO)
 x7 = sfilter(x5, x6)
 x8 = totuple(x7)
 x9 = first(x8)
 x10 = last(x8)
 x11 = ofcolor(I, x9)
 x12 = mapply(neighbors, x11)
 x13 = toobject(x12, I)
 x14 = mostcolor(x13)
 x15 = ofcolor(I, x10)
 x16 = mapply(neighbors, x15)
 x17 = toobject(x16, I)
 x18 = mostcolor(x17)
 x19 = rbind(shoot, UNITY)
 x20 = rbind(shoot, NEG_UNITY)
 x21 = fork(combine, x19, x20)
 x22 = rbind(shoot, UP_RIGHT)
 x23 = rbind(shoot, DOWN_LEFT)
 x24 = fork(combine, x22, x23)
 x25 = fork(combine, x21, x24)
 x26 = ofcolor(I, x10)
 x27 = ofcolor(I, x9)
 x28 = combine(x26, x27)
 x29 = mapply(x25, x28)
 x30 = ofcolor(I, x14)
 x31 = intersection(x30, x29)
 x32 = ofcolor(I, x18)
 x33 = intersection(x32, x29)
 x34 = fill(I, x9, x31)
 x35 = fill(x34, x10, x33)
 return x35
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]