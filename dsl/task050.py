def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def mfilter(
 container,
 function
):
 return merge(sfilter(container, function))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def either(
 a,
 b
):
 return a or b
ONE = 1
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
def size(
 container
):
 return len(container)
def greater(
 a,
 b
):
 return a > b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
THREE = 3
def vline(
 patch
):
 return height(patch) == len(patch) and width(patch) == 1
def prapply(
 function,
 a,
 b
):
 return frozenset(function(i, j) for j in b for i in a)
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
def verify_task050(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = prapply(connect, x1, x1)
 x3 = rbind(greater, ONE)
 x4 = compose(x3, size)
 x5 = sfilter(x2, x4)
 x6 = fork(either, vline, hline)
 x7 = mfilter(x5, x6)
 x8 = fill(I, THREE, x7)
 x9 = leastcolor(I)
 x10 = fill(x8, x9, x1)
 return x10
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]