DOWN_LEFT = (1, -1)
NEG_UNITY = (-1, -1)
ONE = 1
ORIGIN = (0, 0)
UNITY = (1, 1)
UP_RIGHT = (-1, 1)
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def astuple(
 a,
 b
):
 return (a, b)
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
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def flip(
 b
):
 return not b
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
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
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def mfilter(
 container,
 function
):
 return merge(sfilter(container, function))
def mostcommon(
 container
):
 return max(set(container), key=container.count)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(
 element
):
 return len(palette(element))
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
def toivec(
 i
):
 return (i, 0)
def tojvec(
 j
):
 return (0, j)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def vline(
 patch
):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task065(I):
 x0 = frontiers(I)
 x1 = mfilter(x0, hline)
 x2 = mfilter(x0, vline)
 x3 = uppermost(x1)
 x4 = leftmost(x2)
 x5 = astuple(x3, x4)
 x6 = add(x5, NEG_UNITY)
 x7 = uppermost(x1)
 x8 = rightmost(x2)
 x9 = astuple(x7, x8)
 x10 = add(x9, UP_RIGHT)
 x11 = lowermost(x1)
 x12 = leftmost(x2)
 x13 = astuple(x11, x12)
 x14 = add(x13, DOWN_LEFT)
 x15 = lowermost(x1)
 x16 = rightmost(x2)
 x17 = astuple(x15, x16)
 x18 = add(x17, UNITY)
 x19 = initset(ORIGIN)
 x20 = insert(x6, x19)
 x21 = width(I)
 x22 = decrement(x21)
 x23 = tojvec(x22)
 x24 = initset(x23)
 x25 = insert(x10, x24)
 x26 = height(I)
 x27 = decrement(x26)
 x28 = toivec(x27)
 x29 = initset(x28)
 x30 = insert(x14, x29)
 x31 = shape(I)
 x32 = decrement(x31)
 x33 = initset(x32)
 x34 = insert(x18, x33)
 x35 = astuple(x20, x25)
 x36 = astuple(x30, x34)
 x37 = combine(x35, x36)
 x38 = rbind(toobject, I)
 x39 = compose(x38, backdrop)
 x40 = apply(x39, x37)
 x41 = matcher(numcolors, ONE)
 x42 = sfilter(x40, x41)
 x43 = apply(color, x42)
 x44 = mostcommon(x43)
 x45 = initset(x44)
 x46 = matcher(palette, x45)
 x47 = compose(flip, x46)
 x48 = extract(x40, x47)
 x49 = subgrid(x48, I)
 return x49
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]