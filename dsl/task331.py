def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
SEVEN = 7
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
LEFT = (0, -1)
UP = (-1, 0)
RIGHT = (0, 1)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
SIX = 6
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
DOWN = (1, 0)
EIGHT = 8
TWO = 2
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
def verify_task331(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = toindices(x1)
 x3 = shift(x2, DOWN)
 x4 = fill(I, EIGHT, x3)
 x5 = shift(x2, UP)
 x6 = fill(x4, TWO, x5)
 x7 = shift(x2, RIGHT)
 x8 = fill(x6, SIX, x7)
 x9 = shift(x2, LEFT)
 x10 = fill(x8, SEVEN, x9)
 return x10
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]