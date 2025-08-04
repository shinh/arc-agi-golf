def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(
 grid,
 n
):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
UNITY = (1, 1)
NINE = 9
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
ONE = 1
def initset(
 value
):
 return frozenset({value})
def first(
 container
):
 return next(iter(container))
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
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
ORIGIN = (0, 0)
TWO_BY_ZERO = (2, 0)
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
def hconcat(
 a,
 b
):
 return tuple(i + j for i, j in zip(a, b))
def vconcat(
 a,
 b
):
 return a + b
def color(
 obj
):
 return next(iter(obj))[0]
THREE = 3
DOWN = (1, 0)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task316(I):
 x0 = asobject(I)
 x1 = mostcolor(I)
 x2 = matcher(first, x1)
 x3 = compose(flip, x2)
 x4 = sfilter(x0, x3)
 x5 = apply(initset, x4)
 x6 = astuple(ONE, THREE)
 x7 = size(x5)
 x8 = order(x5, leftmost)
 x9 = apply(color, x8)
 x10 = rbind(canvas, UNITY)
 x11 = apply(x10, x9)
 x12 = merge(x11)
 x13 = dmirror(x12)
 x14 = subtract(NINE, x7)
 x15 = astuple(ONE, x14)
 x16 = mostcolor(I)
 x17 = canvas(x16, x15)
 x18 = hconcat(x13, x17)
 x19 = hsplit(x18, THREE)
 x20 = merge(x19)
 x21 = crop(x20, ORIGIN, x6)
 x22 = crop(x20, DOWN, x6)
 x23 = crop(x20, TWO_BY_ZERO, x6)
 x24 = vmirror(x22)
 x25 = vconcat(x21, x24)
 x26 = vconcat(x25, x23)
 return x26
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]