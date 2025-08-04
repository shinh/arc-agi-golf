def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def hperiod(
 obj
):
 normalized = normalize(obj)
 w = width(normalized)
 for p in range(1, w):
  offsetted = shift(normalized, (0, -p))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
  if pruned.issubset(normalized):
   return p
 return w
ORIGIN = (0, 0)
def astuple(
 a,
 b
):
 return (a, b)
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
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task231(I):
 x0 = width(I)
 x1 = asobject(I)
 x2 = hperiod(x1)
 x3 = height(x1)
 x4 = astuple(x3, x2)
 x5 = ulcorner(x1)
 x6 = crop(I, x5, x4)
 x7 = rot90(x6)
 x8 = double(x0)
 x9 = divide(x8, x2)
 x10 = increment(x9)
 x11 = repeat(x7, x10)
 x12 = merge(x11)
 x13 = rot270(x12)
 x14 = astuple(x3, x8)
 x15 = crop(x13, ORIGIN, x14)
 return x15
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]