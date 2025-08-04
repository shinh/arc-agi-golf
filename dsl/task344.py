def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def lbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def positive(
 x
):
 return x > 0
def size(
 container
):
 return len(container)
def intersection(
 a,
 b
):
 return a & b
THREE = 3
EIGHT = 8
TWO = 2
def verify_task344(I):
 x0 = ofcolor(I, TWO)
 x1 = ofcolor(I, THREE)
 x2 = compose(positive, size)
 x3 = lbind(intersection, x1)
 x4 = chain(x2, x3, dneighbors)
 x5 = compose(positive, size)
 x6 = lbind(intersection, x0)
 x7 = chain(x5, x6, dneighbors)
 x8 = sfilter(x0, x4)
 x9 = sfilter(x1, x7)
 x10 = cover(I, x8)
 x11 = fill(x10, EIGHT, x9)
 return x11
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]