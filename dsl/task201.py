def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
UNITY = (1, 1)
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
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
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
def last(
 container
):
 return max(enumerate(container))[1]
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
def shape(
 piece
):
 return (height(piece), width(piece))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def size(
 container
):
 return len(container)
def positive(
 x
):
 return x > 0
def greater(
 a,
 b
):
 return a > b
def identity(
 x
):
 return x
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def color(
 obj
):
 return next(iter(obj))[0]
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def verify_task201(I):
 x0 = partition(I)
 x1 = fork(equality, corners, toindices)
 x2 = extract(x0, x1)
 x3 = subgrid(x2, I)
 x4 = backdrop(x2)
 x5 = cover(I, x4)
 x6 = frontiers(x3)
 x7 = sfilter(x6, hline)
 x8 = size(x7)
 x9 = positive(x8)
 x10 = branch(x9, dmirror, identity)
 x11 = x10(x3)
 x12 = x10(x5)
 x13 = fgpartition(x12)
 x14 = merge(x13)
 x15 = normalize(x14)
 x16 = mostcolor(x12)
 x17 = color(x2)
 x18 = palette(x11)
 x19 = remove(x17, x18)
 x20 = remove(x16, x19)
 x21 = first(x20)
 x22 = last(x20)
 x23 = ofcolor(x11, x22)
 x24 = leftmost(x23)
 x25 = ofcolor(x11, x21)
 x26 = leftmost(x25)
 x27 = greater(x24, x26)
 x28 = ofcolor(x12, x22)
 x29 = leftmost(x28)
 x30 = ofcolor(x12, x21)
 x31 = leftmost(x30)
 x32 = greater(x29, x31)
 x33 = equality(x27, x32)
 x34 = branch(x33, identity, vmirror)
 x35 = x34(x15)
 x36 = shift(x35, UNITY)
 x37 = paint(x11, x36)
 x38 = x10(x37)
 return x38
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]