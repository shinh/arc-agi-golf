def toivec(
 i
):
 return (i, 0)
def tojvec(
 j
):
 return (0, j)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def flip(
 b
):
 return not b
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
def astuple(
 a,
 b
):
 return (a, b)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def verify_task253(I):
 x0 = fgpartition(I)
 x1 = fork(contained, lrcorner, toindices)
 x2 = compose(flip, x1)
 x3 = extract(x0, x2)
 x4 = fork(contained, llcorner, toindices)
 x5 = compose(flip, x4)
 x6 = extract(x0, x5)
 x7 = fork(contained, urcorner, toindices)
 x8 = compose(flip, x7)
 x9 = extract(x0, x8)
 x10 = fork(contained, ulcorner, toindices)
 x11 = compose(flip, x10)
 x12 = extract(x0, x11)
 x13 = height(x3)
 x14 = height(x9)
 x15 = add(x13, x14)
 x16 = width(x3)
 x17 = width(x6)
 x18 = add(x16, x17)
 x19 = astuple(x15, x18)
 x20 = mostcolor(I)
 x21 = canvas(x20, x19)
 x22 = normalize(x3)
 x23 = paint(x21, x22)
 x24 = normalize(x6)
 x25 = width(x6)
 x26 = subtract(x18, x25)
 x27 = tojvec(x26)
 x28 = shift(x24, x27)
 x29 = paint(x23, x28)
 x30 = normalize(x9)
 x31 = height(x9)
 x32 = subtract(x15, x31)
 x33 = toivec(x32)
 x34 = shift(x30, x33)
 x35 = paint(x29, x34)
 x36 = normalize(x12)
 x37 = shape(x12)
 x38 = subtract(x19, x37)
 x39 = shift(x36, x38)
 x40 = paint(x35, x39)
 return x40
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]