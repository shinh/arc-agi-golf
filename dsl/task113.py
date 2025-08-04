ONE = 1
TWO = 2
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def contained(
 value,
 container
):
 return value in container
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
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
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task113(I):
 x0 = mostcolor(I)
 x1 = vsplit(I, TWO)
 x2 = apply(numcolors, x1)
 x3 = contained(ONE, x2)
 x4 = branch(x3, hmirror, vmirror)
 x5 = x4(I)
 x6 = asobject(x5)
 x7 = matcher(first, x0)
 x8 = compose(flip, x7)
 x9 = sfilter(x6, x8)
 x10 = paint(I, x9)
 return x10
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]