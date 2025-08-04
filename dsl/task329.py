def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
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
def flip(
 b
):
 return not b
def both(
 a,
 b
):
 return a and b
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def verify_task329(I):
 x0 = mostcolor(I)
 x1 = matcher(first, x0)
 x2 = compose(flip, x1)
 x3 = width(I)
 x4 = halve(x3)
 x5 = compose(last, last)
 x6 = matcher(x5, x4)
 x7 = compose(flip, x6)
 x8 = asobject(I)
 x9 = fork(both, x2, x7)
 x10 = sfilter(x8, x9)
 x11 = fill(I, x0, x10)
 return x11
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]