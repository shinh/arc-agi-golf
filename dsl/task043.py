def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def either(
 a,
 b
):
 return a or b
def initset(
 value
):
 return frozenset({value})
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
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
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def size(
 container
):
 return len(container)
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
TWO = 2
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
def verify_task043(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = apply(first, x1)
 x3 = apply(last, x1)
 x4 = product(x2, x3)
 x5 = difference(x4, x1)
 x6 = fill(I, TWO, x5)
 x7 = lbind(fork, either)
 x8 = lbind(matcher, first)
 x9 = compose(x8, first)
 x10 = lbind(matcher, last)
 x11 = compose(x10, last)
 x12 = fork(x7, x9, x11)
 x13 = lbind(sfilter, x1)
 x14 = chain(size, x13, x12)
 x15 = asindices(I)
 x16 = corners(x15)
 x17 = argmax(x16, x14)
 x18 = mostcolor(I)
 x19 = initset(x17)
 x20 = fill(x6, x18, x19)
 return x20
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]