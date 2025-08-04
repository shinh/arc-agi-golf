EIGHT = 8
THREE = 3
TWO = 2
def astuple(
 a,
 b
):
 return (a, b)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def connect(
 a,
 b
):
 ai, aj = a
 bi, bj = b
 si = min(ai, bi)
 ei = max(ai, bi) + 1
 sj = min(aj, bj)
 ej = max(aj, bj) + 1
 if ai == bi:
  return frozenset((ai, j) for j in range(sj, ej))
 elif aj == bj:
  return frozenset((i, aj) for i in range(si, ei))
 elif bi - ai == bj - aj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
 elif bi - ai == aj - bj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
 return frozenset()
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
def maximum(
 container
):
 return max(container, default=0)
def minimum(
 container
):
 return min(container, default=0)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def underfill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 bg = mostcolor(grid)
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   if grid_filled[i][j] == bg:
    grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def verify_task246(I):
 x0 = ofcolor(I, TWO)
 x1 = ofcolor(I, THREE)
 x2 = uppermost(x0)
 x3 = leftmost(x0)
 x4 = uppermost(x1)
 x5 = leftmost(x1)
 x6 = astuple(x2, x4)
 x7 = minimum(x6)
 x8 = maximum(x6)
 x9 = astuple(x7, x5)
 x10 = astuple(x8, x5)
 x11 = connect(x9, x10)
 x12 = astuple(x3, x5)
 x13 = minimum(x12)
 x14 = maximum(x12)
 x15 = astuple(x2, x13)
 x16 = astuple(x2, x14)
 x17 = connect(x15, x16)
 x18 = combine(x11, x17)
 x19 = underfill(I, EIGHT, x18)
 return x19
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]