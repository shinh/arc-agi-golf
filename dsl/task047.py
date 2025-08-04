def combine(
 a,
 b
):
 return type(a)((*a, *b))
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def hfrontier(
 location
):
 return frozenset((location[0], j) for j in range(30))
def vfrontier(
 location
):
 return frozenset((i, location[1]) for i in range(30))
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
TWO = 2
def totuple(
 container
):
 return tuple(container)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def verify_task047(I):
 x0 = mostcolor(I)
 x1 = palette(I)
 x2 = remove(x0, x1)
 x3 = totuple(x2)
 x4 = fork(combine, hfrontier, vfrontier)
 x5 = lbind(mapply, x4)
 x6 = lbind(ofcolor, I)
 x7 = compose(x5, x6)
 x8 = first(x3)
 x9 = last(x3)
 x10 = x7(x8)
 x11 = x7(x9)
 x12 = ofcolor(I, x0)
 x13 = intersection(x12, x10)
 x14 = intersection(x12, x11)
 x15 = intersection(x10, x11)
 x16 = intersection(x12, x15)
 x17 = fill(I, x8, x13)
 x18 = fill(x17, x9, x14)
 x19 = fill(x18, TWO, x16)
 return x19
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]