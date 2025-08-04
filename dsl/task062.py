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
def toivec(
 i
):
 return (i, 0)
def tojvec(
 j
):
 return (0, j)
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def hmatching(
 a,
 b
):
 return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0
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
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def size(
 container
):
 return len(container)
def greater(
 a,
 b
):
 return a > b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
THREE = 3
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
def verify_task062(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = argmax(x0, x1)
 x3 = remove(x2, x0)
 x4 = argmin(x3, size)
 x5 = argmax(x3, size)
 x6 = hmatching(x4, x5)
 x7 = branch(x6, vmirror, hmirror)
 x8 = x7(x5)
 x9 = branch(x6, leftmost, uppermost)
 x10 = branch(x6, tojvec, toivec)
 x11 = x9(x4)
 x12 = x9(x5)
 x13 = greater(x11, x12)
 x14 = double(x13)
 x15 = decrement(x14)
 x16 = x10(x15)
 x17 = shape(x5)
 x18 = multiply(x16, x17)
 x19 = shift(x8, x18)
 x20 = fill(I, THREE, x2)
 x21 = paint(x20, x19)
 return x21
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]