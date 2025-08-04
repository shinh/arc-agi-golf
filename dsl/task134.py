def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def switch(
 grid,
 a,
 b
):
 return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)
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
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def maximum(
 container
):
 return max(container, default=0)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
ONE = 1
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
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
def flip(
 b
):
 return not b
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def size(
 container
):
 return len(container)
def positive(
 x
):
 return x > 0
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def identity(
 x
):
 return x
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
def add(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
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
def upscale(
 element,
 factor
):
 if isinstance(element, tuple):
  upscaled_grid = tuple()
  for row in element:
   upscaled_row = tuple()
   for value in row:
    upscaled_row = upscaled_row + tuple(value for num in range(factor))
   upscaled_grid = upscaled_grid + tuple(upscaled_row for num in range(factor))
  return upscaled_grid
 else:
  if len(element) == 0:
   return frozenset()
  di_inv, dj_inv = ulcorner(element)
  di, dj = (-di_inv, -dj_inv)
  normed_obj = shift(element, (di, dj))
  upscaled_obj = set()
  for value, (i, j) in normed_obj:
   for io in range(factor):
    for jo in range(factor):
     upscaled_obj.add((value, (i * factor + io, j * factor + jo)))
  return shift(frozenset(upscaled_obj), (di_inv, dj_inv))
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def downscale(
 grid,
 factor
):
 h, w = len(grid), len(grid[0])
 downscaled_grid = tuple()
 for i in range(h):
  downscaled_row = tuple()
  for j in range(w):
   if j % factor == 0:
    downscaled_row = downscaled_row + (grid[i][j],)
  downscaled_grid = downscaled_grid + (downscaled_row, )
 h = len(downscaled_grid)
 downscaled_grid2 = tuple()
 for i in range(h):
  if i % factor == 0:
   downscaled_grid2 = downscaled_grid2 + (downscaled_grid[i],)
 return downscaled_grid2
def verify_task134(I):
 x0 = asindices(I)
 x1 = box(x0)
 x2 = toobject(x1, I)
 x3 = mostcolor(x2)
 x4 = palette(I)
 x5 = remove(x3, x4)
 x6 = lbind(chain, size)
 x7 = rbind(x6, dneighbors)
 x8 = lbind(lbind, intersection)
 x9 = lbind(ofcolor, I)
 x10 = chain(x7, x8, x9)
 x11 = rbind(matcher, ZERO)
 x12 = compose(x11, x10)
 x13 = chain(flip, positive, size)
 x14 = lbind(ofcolor, I)
 x15 = fork(sfilter, x14, x12)
 x16 = compose(x13, x15)
 x17 = argmax(x5, x16)
 x18 = other(x5, x17)
 x19 = ofcolor(I, x17)
 x20 = subgrid(x19, I)
 x21 = switch(x20, x17, x18)
 x22 = replace(x21, x17, x3)
 x23 = lbind(downscale, x22)
 x24 = fork(upscale, x23, identity)
 x25 = matcher(x24, x22)
 x26 = shape(x22)
 x27 = maximum(x26)
 x28 = interval(ONE, x27, ONE)
 x29 = sfilter(x28, x25)
 x30 = maximum(x29)
 x31 = downscale(x22, x30)
 return x31
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]