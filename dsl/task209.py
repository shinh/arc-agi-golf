def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mostcommon(
 container
):
 return max(set(container), key=container.count)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def pair(
 a,
 b
):
 return tuple(zip(a, b))
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
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
def last(
 container
):
 return max(enumerate(container))[1]
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def flip(
 b
):
 return not b
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
def divide(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def size(
 container
):
 return len(container)
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
def identity(
 x
):
 return x
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def vupscale(
 grid,
 factor
):
 upscaled_grid = tuple()
 for row in grid:
  upscaled_grid = upscaled_grid + tuple(row for num in range(factor))
 return upscaled_grid
def contained(
 value,
 container
):
 return value in container
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
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
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
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
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task209(I):
 x0 = partition(I)
 x1 = fork(equality, toindices, corners)
 x2 = sfilter(x0, x1)
 x3 = argmax(x2, size)
 x4 = fgpartition(I)
 x5 = merge(x4)
 x6 = backdrop(x3)
 x7 = toobject(x6, I)
 x8 = difference(x5, x7)
 x9 = mostcolor(I)
 x10 = inbox(x3)
 x11 = backdrop(x10)
 x12 = toobject(x11, I)
 x13 = matcher(first, x9)
 x14 = compose(flip, x13)
 x15 = sfilter(x12, x14)
 x16 = subgrid(x8, I)
 x17 = palette(x15)
 x18 = order(x17, identity)
 x19 = lbind(colorcount, x15)
 x20 = apply(x19, x18)
 x21 = lbind(colorcount, x8)
 x22 = apply(x21, x18)
 x23 = pair(x20, x22)
 x24 = fork(divide, first, last)
 x25 = apply(x24, x23)
 x26 = mostcommon(x25)
 x27 = lbind(colorcount, x15)
 x28 = lbind(colorcount, x8)
 x29 = fork(divide, x27, x28)
 x30 = matcher(x29, x26)
 x31 = palette(x8)
 x32 = sfilter(x31, x30)
 x33 = rbind(contained, x32)
 x34 = compose(x33, first)
 x35 = sfilter(x15, x34)
 x36 = sfilter(x8, x34)
 x37 = height(x35)
 x38 = height(x36)
 x39 = divide(x37, x38)
 x40 = width(x35)
 x41 = width(x36)
 x42 = divide(x40, x41)
 x43 = vupscale(x16, x39)
 x44 = hupscale(x43, x42)
 x45 = asobject(x44)
 x46 = matcher(first, x9)
 x47 = compose(flip, x46)
 x48 = sfilter(x45, x47)
 x49 = ulcorner(x15)
 x50 = sfilter(x48, x34)
 x51 = ulcorner(x50)
 x52 = subtract(x49, x51)
 x53 = shift(x48, x52)
 x54 = paint(I, x53)
 x55 = subgrid(x3, x54)
 return x55
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]