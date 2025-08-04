def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def tojvec(
 j
):
 return (0, j)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
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
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
ONE = 1
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
def initset(
 value
):
 return frozenset({value})
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def hperiod(
 obj
):
 normalized = normalize(obj)
 w = width(normalized)
 for p in range(1, w):
  offsetted = shift(normalized, (0, -p))
  pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
  if pruned.issubset(normalized):
   return p
 return w
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
def both(
 a,
 b
):
 return a and b
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
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task343(I):
 x0 = astuple(identity, rot90)
 x1 = astuple(rot180, rot270)
 x2 = combine(x0, x1)
 x3 = astuple(identity, rot270)
 x4 = astuple(rot180, rot90)
 x5 = combine(x3, x4)
 x6 = pair(x2, x5)
 x7 = chain(size, dedupe, first)
 x8 = matcher(x7, ONE)
 x9 = compose(first, cmirror)
 x10 = chain(size, dedupe, x9)
 x11 = matcher(x10, ONE)
 x12 = fork(both, x8, x11)
 x13 = rbind(rapply, I)
 x14 = compose(initset, first)
 x15 = chain(first, x13, x14)
 x16 = compose(x12, x15)
 x17 = extract(x6, x16)
 x18 = first(x17)
 x19 = last(x17)
 x20 = x18(I)
 x21 = width(x20)
 x22 = decrement(x21)
 x23 = tojvec(x22)
 x24 = index(x20, x23)
 x25 = asobject(x20)
 x26 = matcher(first, x24)
 x27 = compose(flip, x26)
 x28 = sfilter(x25, x27)
 x29 = hperiod(x28)
 x30 = width(x20)
 x31 = increment(x30)
 x32 = interval(ZERO, x31, x29)
 x33 = apply(tojvec, x32)
 x34 = lbind(shift, x28)
 x35 = mapply(x34, x33)
 x36 = paint(x20, x35)
 x37 = x19(x36)
 return x37
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]