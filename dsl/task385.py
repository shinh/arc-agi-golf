ONE = 1
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def bottomhalf(
 grid
):
 return grid[len(grid) // 2 + len(grid) % 2:]
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
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
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def either(
 a,
 b
):
 return a or b
def equality(
 a,
 b
):
 return a == b
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(
 x
):
 return x
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def numcolors(
 element
):
 return len(palette(element))
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def tophalf(
 grid
):
 return grid[:len(grid) // 2]
def verify_task385(I):
 x0 = tophalf(I)
 x1 = numcolors(x0)
 x2 = equality(x1, ONE)
 x3 = bottomhalf(I)
 x4 = numcolors(x3)
 x5 = equality(x4, ONE)
 x6 = either(x2, x5)
 x7 = branch(x6, identity, dmirror)
 x8 = x7(I)
 x9 = asobject(x8)
 x10 = hmirror(x9)
 x11 = mostcolor(I)
 x12 = matcher(first, x11)
 x13 = compose(flip, x12)
 x14 = sfilter(x10, x13)
 x15 = paint(x8, x14)
 x16 = x7(x15)
 return x16
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]