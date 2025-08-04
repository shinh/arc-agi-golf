ONE = 1
SEVEN = 7
THREE = 3
TWO = 2
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def cover(
 grid,
 patch
):
 return fill(grid, mostcolor(grid), toindices(patch))
def initset(
 value
):
 return frozenset({value})
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def position(
 a,
 b
):
 ia, ja = center(toindices(a))
 ib, jb = center(toindices(b))
 if ia == ib:
  return (0, 1 if ja < jb else -1)
 elif ja == jb:
  return (1 if ia < ib else -1, 0)
 elif ia < ib:
  return (1, 1 if ja < jb else -1)
 elif ia > ib:
  return (-1, 1 if ja < jb else -1)
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
def verify_task270(I):
 x0 = ofcolor(I, ONE)
 x1 = center(x0)
 x2 = ofcolor(I, TWO)
 x3 = center(x2)
 x4 = ofcolor(I, THREE)
 x5 = ofcolor(I, SEVEN)
 x6 = lbind(add, x1)
 x7 = initset(x1)
 x8 = rbind(position, x7)
 x9 = compose(invert, x8)
 x10 = chain(x6, x9, initset)
 x11 = lbind(add, x3)
 x12 = initset(x3)
 x13 = rbind(position, x12)
 x14 = compose(invert, x13)
 x15 = chain(x11, x14, initset)
 x16 = apply(x10, x5)
 x17 = apply(x15, x4)
 x18 = combine(x4, x5)
 x19 = cover(I, x18)
 x20 = fill(x19, SEVEN, x16)
 x21 = fill(x20, THREE, x17)
 return x21
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]