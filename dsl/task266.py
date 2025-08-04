DOWN_LEFT = (1, -1)
EIGHT = 8
NEG_UNITY = (-1, -1)
SEVEN = 7
SIX = 6
THREE = 3
UNITY = (1, 1)
UP_RIGHT = (-1, 1)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
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
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(
 grid,
 obj
):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
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
def verify_task266(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = shift(x1, NEG_UNITY)
 x3 = recolor(THREE, x2)
 x4 = shift(x1, UNITY)
 x5 = recolor(SEVEN, x4)
 x6 = shift(x1, DOWN_LEFT)
 x7 = recolor(EIGHT, x6)
 x8 = shift(x1, UP_RIGHT)
 x9 = recolor(SIX, x8)
 x10 = mostcolor(I)
 x11 = fill(I, x10, x1)
 x12 = combine(x3, x5)
 x13 = combine(x7, x9)
 x14 = combine(x12, x13)
 x15 = paint(x11, x14)
 return x15
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]