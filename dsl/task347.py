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
TWO_BY_TWO = (2, 2)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(
 grid,
 n
):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
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
def shape(
 piece
):
 return (height(piece), width(piece))
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def last(
 container
):
 return max(enumerate(container))[1]
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
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def intersection(
 a,
 b
):
 return a & b
SIX = 6
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
def verify_task347(I):
 x0 = hsplit(I, TWO)
 x1 = apply(numcolors, x0)
 x2 = equality(x1, TWO_BY_TWO)
 x3 = branch(x2, hsplit, vsplit)
 x4 = x3(I, TWO)
 x5 = first(x4)
 x6 = last(x4)
 x7 = palette(x5)
 x8 = palette(x6)
 x9 = intersection(x7, x8)
 x10 = first(x9)
 x11 = palette(x5)
 x12 = other(x11, x10)
 x13 = palette(x6)
 x14 = other(x13, x10)
 x15 = shape(x5)
 x16 = canvas(x10, x15)
 x17 = ofcolor(x5, x12)
 x18 = ofcolor(x6, x14)
 x19 = combine(x17, x18)
 x20 = fill(x16, SIX, x19)
 return x20
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]