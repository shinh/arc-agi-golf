FOUR = 4
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
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
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
def first(
 container
):
 return next(iter(container))
def intersection(
 a,
 b
):
 return a & b
def last(
 container
):
 return max(enumerate(container))[1]
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def outbox(
 patch
):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def totuple(
 container
):
 return tuple(container)
def verify_task151(I):
 x0 = mostcolor(I)
 x1 = palette(I)
 x2 = remove(x0, x1)
 x3 = totuple(x2)
 x4 = first(x3)
 x5 = last(x3)
 x6 = ofcolor(I, x4)
 x7 = backdrop(x6)
 x8 = ofcolor(I, x5)
 x9 = backdrop(x8)
 x10 = intersection(x7, x9)
 x11 = outbox(x10)
 x12 = fill(I, FOUR, x11)
 return x12
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]