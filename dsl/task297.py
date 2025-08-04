ONE = 1
TWO_BY_ZERO = (2, 0)
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(
 a,
 b
):
 return (a, b)
def both(
 a,
 b
):
 return a and b
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
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
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def first(
 container
):
 return next(iter(container))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def greater(
 a,
 b
):
 return a > b
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def hupscale(
 grid,
 factor
):
 upscaled_grid = tuple()
 for row in grid:
  upscaled_row = tuple()
  for value in row:
   upscaled_row = upscaled_row + tuple(value for num in range(factor))
  upscaled_grid = upscaled_grid + (upscaled_row,)
 return upscaled_grid
def identity(
 x
):
 return x
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
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
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
def positive(
 x
):
 return x > 0
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
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def shift(
 patch,
 directions
):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def size(
 container
):
 return len(container)
def toivec(
 i
):
 return (i, 0)
def verify_task297(I):
 x0 = compose(positive, size)
 x1 = rbind(sfilter, hline)
 x2 = chain(x0, x1, frontiers)
 x3 = chain(size, dedupe, first)
 x4 = chain(size, dedupe, last)
 x5 = fork(greater, x3, x4)
 x6 = fork(both, x2, x5)
 x7 = astuple(identity, rot90)
 x8 = astuple(rot180, rot270)
 x9 = combine(x7, x8)
 x10 = astuple(identity, rot270)
 x11 = astuple(rot180, rot90)
 x12 = combine(x10, x11)
 x13 = pair(x9, x12)
 x14 = rbind(rapply, I)
 x15 = compose(initset, first)
 x16 = chain(first, x14, x15)
 x17 = compose(x6, x16)
 x18 = extract(x13, x17)
 x19 = first(x18)
 x20 = last(x18)
 x21 = x19(I)
 x22 = first(x21)
 x23 = repeat(x22, ONE)
 x24 = dmirror(x23)
 x25 = width(x21)
 x26 = hupscale(x24, x25)
 x27 = asobject(x26)
 x28 = height(x21)
 x29 = height(x27)
 x30 = interval(ZERO, x28, x29)
 x31 = lbind(shift, x27)
 x32 = apply(toivec, x30)
 x33 = mapply(x31, x32)
 x34 = shift(x33, TWO_BY_ZERO)
 x35 = paint(x21, x34)
 x36 = x20(x35)
 return x36
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]