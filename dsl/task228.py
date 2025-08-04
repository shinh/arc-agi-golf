def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
DOWN_LEFT = (1, -1)
UNITY = (1, 1)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
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
def cover(
 grid,
 patch
):
 return fill(grid, mostcolor(grid), toindices(patch))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
NEG_UNITY = (-1, -1)
def initset(
 value
):
 return frozenset({value})
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
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def inbox(
 patch
):
 ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
 bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
UP_RIGHT = (-1, 1)
def verify_task228(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = inbox(x1)
 x3 = cover(I, x2)
 x4 = ulcorner(x2)
 x5 = index(I, x4)
 x6 = lrcorner(x1)
 x7 = add(UNITY, x6)
 x8 = initset(x7)
 x9 = fill(x3, x5, x8)
 x10 = lrcorner(x2)
 x11 = index(I, x10)
 x12 = ulcorner(x1)
 x13 = add(NEG_UNITY, x12)
 x14 = initset(x13)
 x15 = fill(x9, x11, x14)
 x16 = urcorner(x2)
 x17 = index(I, x16)
 x18 = llcorner(x1)
 x19 = add(DOWN_LEFT, x18)
 x20 = initset(x19)
 x21 = fill(x15, x17, x20)
 x22 = llcorner(x2)
 x23 = index(I, x22)
 x24 = urcorner(x1)
 x25 = add(UP_RIGHT, x24)
 x26 = initset(x25)
 x27 = fill(x21, x23, x26)
 return x27
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]