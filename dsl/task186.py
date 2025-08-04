def tojvec(
 j
):
 return (0, j)
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
THREE_BY_THREE = (3, 3)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
ONE = 1
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def initset(
 value
):
 return frozenset({value})
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
def equality(
 a,
 b
):
 return a == b
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
ORIGIN = (0, 0)
FOUR = 4
TWO = 2
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
def verify_task186(I):
 x0 = palette(I)
 x1 = remove(ONE, x0)
 x2 = lbind(colorcount, I)
 x3 = argmax(x1, x2)
 x4 = canvas(x3, THREE_BY_THREE)
 x5 = colorcount(I, ONE)
 x6 = decrement(x5)
 x7 = tojvec(x6)
 x8 = connect(ORIGIN, x7)
 x9 = fill(x4, TWO, x8)
 x10 = initset(UNITY)
 x11 = equality(x5, FOUR)
 x12 = branch(x11, x10, x8)
 x13 = fill(x9, TWO, x12)
 return x13
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]