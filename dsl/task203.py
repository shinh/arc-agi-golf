ONE = 1
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def box(
 patch
):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def color(
 obj
):
 return next(iter(obj))[0]
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
def first(
 container
):
 return next(iter(container))
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def inbox(
 patch
):
 ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
 bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def initset(
 value
):
 return frozenset({value})
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def last(
 container
):
 return max(enumerate(container))[1]
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
def minimum(
 container
):
 return min(container, default=0)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def papply(
 function,
 a,
 b
):
 return tuple(function(i, j) for i, j in zip(a, b))
def mpapply(
 function,
 a,
 b
):
 return merge(papply(function, a, b))
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
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
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
def rbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def width(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def verify_task203(I):
 x0 = asindices(I)
 x1 = box(x0)
 x2 = shape(I)
 x3 = minimum(x2)
 x4 = halve(x3)
 x5 = interval(ONE, x4, ONE)
 x6 = lbind(power, inbox)
 x7 = rbind(rapply, x1)
 x8 = compose(initset, x6)
 x9 = chain(first, x7, x8)
 x10 = apply(x9, x5)
 x11 = repeat(x1, ONE)
 x12 = combine(x11, x10)
 x13 = rbind(toobject, I)
 x14 = compose(color, x13)
 x15 = apply(x14, x12)
 x16 = interval(ZERO, x4, ONE)
 x17 = pair(x16, x15)
 x18 = compose(invert, first)
 x19 = order(x17, x18)
 x20 = apply(last, x19)
 x21 = mpapply(recolor, x20, x12)
 x22 = paint(I, x21)
 return x22
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]