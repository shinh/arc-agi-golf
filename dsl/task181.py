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
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
THREE_BY_THREE = (3, 3)
FIVE = 5
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
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def box(
 patch
):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def either(
 a,
 b
):
 return a or b
ONE = 1
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
def last(
 container
):
 return max(enumerate(container))[1]
def equality(
 a,
 b
):
 return a == b
LEFT = (0, -1)
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
FOUR = 4
UP = (-1, 0)
def size(
 container
):
 return len(container)
def both(
 a,
 b
):
 return a and b
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
def intersection(
 a,
 b
):
 return a & b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
DOWN = (1, 0)
TWO = 2
def verify_task181(I):
 x0 = fgpartition(I)
 x1 = matcher(shape, THREE_BY_THREE)
 x2 = matcher(size, FIVE)
 x3 = fork(intersection, toindices, box)
 x4 = compose(size, x3)
 x5 = matcher(x4, FOUR)
 x6 = fork(intersection, toindices, corners)
 x7 = compose(size, x6)
 x8 = matcher(x7, ONE)
 x9 = fork(both, x1, x2)
 x10 = fork(both, x5, x8)
 x11 = fork(both, x9, x10)
 x12 = extract(x0, x11)
 x13 = toindices(x12)
 x14 = lowermost(x12)
 x15 = matcher(first, x14)
 x16 = uppermost(x12)
 x17 = matcher(first, x16)
 x18 = rightmost(x12)
 x19 = matcher(last, x18)
 x20 = leftmost(x12)
 x21 = matcher(last, x20)
 x22 = sfilter(x13, x15)
 x23 = size(x22)
 x24 = equality(x23, TWO)
 x25 = sfilter(x13, x17)
 x26 = size(x25)
 x27 = equality(x26, TWO)
 x28 = sfilter(x13, x19)
 x29 = size(x28)
 x30 = equality(x29, TWO)
 x31 = sfilter(x13, x21)
 x32 = size(x31)
 x33 = equality(x32, TWO)
 x34 = either(x24, x27)
 x35 = branch(x34, hmirror, vmirror)
 x36 = multiply(x24, DOWN)
 x37 = multiply(x27, UP)
 x38 = add(x36, x37)
 x39 = multiply(x30, RIGHT)
 x40 = multiply(x33, LEFT)
 x41 = add(x39, x40)
 x42 = add(x38, x41)
 x43 = other(x0, x12)
 x44 = x35(x43)
 x45 = shape(x43)
 x46 = multiply(x45, x42)
 x47 = shift(x44, x46)
 x48 = paint(I, x47)
 return x48
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]