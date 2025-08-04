EIGHT = 8
ONE = 1
ZERO = 0
def astuple(
 a,
 b
):
 return (a, b)
def bottomhalf(
 grid
):
 return grid[len(grid) // 2 + len(grid) % 2:]
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
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def equality(
 a,
 b
):
 return a == b
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
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def intersection(
 a,
 b
):
 return a & b
def tophalf(
 grid
):
 return grid[:len(grid) // 2]
def lefthalf(
 grid
):
 return rot270(tophalf(rot90(grid)))
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
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def righthalf(
 grid
):
 return rot270(bottomhalf(rot90(grid)))
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
def tojvec(
 j
):
 return (0, j)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def verify_task026(I):
 x0 = width(I)
 x1 = halve(x0)
 x2 = tojvec(x1)
 x3 = height(I)
 x4 = decrement(x3)
 x5 = astuple(x4, x1)
 x6 = connect(x2, x5)
 x7 = toobject(x6, I)
 x8 = numcolors(x7)
 x9 = equality(x8, ONE)
 x10 = branch(x9, lefthalf, tophalf)
 x11 = branch(x9, righthalf, bottomhalf)
 x12 = x10(I)
 x13 = x11(I)
 x14 = shape(x12)
 x15 = canvas(ZERO, x14)
 x16 = ofcolor(x12, ZERO)
 x17 = ofcolor(x13, ZERO)
 x18 = intersection(x16, x17)
 x19 = fill(x15, EIGHT, x18)
 return x19
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]