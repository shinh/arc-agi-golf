TWO_BY_TWO = (2, 2)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
THREE_BY_THREE = (3, 3)
FIVE = 5
UNITY = (1, 1)
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
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
ZERO = 0
def hfrontier(
 location
):
 return frozenset((location[0], j) for j in range(30))
RIGHT = (0, 1)
def vfrontier(
 location
):
 return frozenset((i, location[1]) for i in range(30))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def contained(
 value,
 container
):
 return value in container
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
def verify_task334(I):
 x0 = palette(I)
 x1 = contained(ONE, x0)
 x2 = contained(TWO, x0)
 x3 = branch(x1, UNITY, TWO_BY_TWO)
 x4 = branch(x2, RIGHT, x3)
 x5 = fork(combine, vfrontier, hfrontier)
 x6 = x5(x4)
 x7 = canvas(ZERO, THREE_BY_THREE)
 x8 = fill(x7, FIVE, x6)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]