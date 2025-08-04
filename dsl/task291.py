def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
UNITY = (1, 1)
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
def color(
 obj
):
 return next(iter(obj))[0]
def flip(
 b
):
 return not b
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def equality(
 a,
 b
):
 return a == b
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def verify_task291(I):
 x0 = fgpartition(I)
 x1 = fork(equality, toindices, backdrop)
 x2 = compose(flip, x1)
 x3 = extract(x0, x2)
 x4 = color(x3)
 x5 = canvas(x4, UNITY)
 return x5
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]