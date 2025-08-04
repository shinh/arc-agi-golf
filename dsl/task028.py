def toivec(
 i
):
 return (i, 0)
def tojvec(
 j
):
 return (0, j)
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
ORIGIN = (0, 0)
def astuple(
 a,
 b
):
 return (a, b)
def bottomhalf(
 grid
):
 return grid[len(grid) // 2 + len(grid) % 2:]
def tophalf(
 grid
):
 return grid[:len(grid) // 2]
def hfrontier(
 location
):
 return frozenset((location[0], j) for j in range(30))
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def verify_task028(I):
 x0 = tophalf(I)
 x1 = bottomhalf(I)
 x2 = leastcolor(x0)
 x3 = leastcolor(x1)
 x4 = ofcolor(I, x2)
 x5 = center(x4)
 x6 = ofcolor(I, x3)
 x7 = center(x6)
 x8 = height(I)
 x9 = width(I)
 x10 = hfrontier(x5)
 x11 = fill(I, x2, x10)
 x12 = hfrontier(x7)
 x13 = fill(x11, x3, x12)
 x14 = decrement(x9)
 x15 = decrement(x8)
 x16 = halve(x8)
 x17 = tojvec(x14)
 x18 = connect(ORIGIN, x17)
 x19 = fill(x13, x2, x18)
 x20 = toivec(x15)
 x21 = astuple(x15, x14)
 x22 = connect(x20, x21)
 x23 = fill(x19, x3, x22)
 x24 = decrement(x16)
 x25 = toivec(x24)
 x26 = connect(ORIGIN, x25)
 x27 = fill(x23, x2, x26)
 x28 = tojvec(x14)
 x29 = decrement(x16)
 x30 = astuple(x29, x14)
 x31 = connect(x28, x30)
 x32 = fill(x27, x2, x31)
 x33 = toivec(x16)
 x34 = toivec(x15)
 x35 = connect(x33, x34)
 x36 = fill(x32, x3, x35)
 x37 = astuple(x16, x14)
 x38 = astuple(x15, x14)
 x39 = connect(x37, x38)
 x40 = fill(x36, x3, x39)
 return x40
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]