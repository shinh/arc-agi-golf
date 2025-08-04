THREE = 3
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def equality(
 a,
 b
):
 return a == b
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def identity(
 x
):
 return x
def last(
 container
):
 return max(enumerate(container))[1]
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def verify_task332(I):
 x0 = vmirror(I)
 x1 = fgpartition(x0)
 x2 = merge(x1)
 x3 = toindices(x2)
 x4 = compose(double, halve)
 x5 = fork(equality, identity, x4)
 x6 = compose(x5, last)
 x7 = sfilter(x3, x6)
 x8 = fill(x0, THREE, x7)
 x9 = vmirror(x8)
 return x9
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]