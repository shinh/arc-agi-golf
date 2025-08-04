FIVE = 5
FOUR = 4
ONE = 1
SEVEN = 7
THREE = 3
UNITY = (1, 1)
ZERO = 0
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
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def both(
 a,
 b
):
 return a and b
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
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
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
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def even(
 n
):
 return n % 2 == 0
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(
 x
):
 return x
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
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def minimum(
 container
):
 return min(container, default=0)
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
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
def positive(
 x
):
 return x > 0
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def shape(
 piece
):
 return (height(piece), width(piece))
def size(
 container
):
 return len(container)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def trim(
 grid
):
 return tuple(r[1:-1] for r in grid[1:-1])
def verify_task020(I):
 x0 = mostcolor(I)
 x1 = lbind(remove, x0)
 x2 = chain(positive, size, x1)
 x3 = compose(x2, palette)
 x4 = multiply(FIVE, UNITY)
 x5 = canvas(ZERO, x4)
 x6 = asindices(x5)
 x7 = fork(add, first, last)
 x8 = chain(flip, even, x7)
 x9 = sfilter(x6, x8)
 x10 = initset(x0)
 x11 = box(x6)
 x12 = inbox(x6)
 x13 = center(x6)
 x14 = initset(x13)
 x15 = lbind(toobject, x11)
 x16 = compose(x3, x15)
 x17 = lbind(toobject, x12)
 x18 = compose(x3, x17)
 x19 = lbind(toobject, x14)
 x20 = compose(x3, x19)
 x21 = fork(both, x18, x20)
 x22 = fork(both, x16, x21)
 x23 = compose(x22, trim)
 x24 = compose(box, asindices)
 x25 = fork(toobject, x24, identity)
 x26 = compose(palette, x25)
 x27 = matcher(x26, x10)
 x28 = lbind(toobject, x9)
 x29 = chain(palette, x28, trim)
 x30 = matcher(x29, x10)
 x31 = compose(minimum, shape)
 x32 = chain(x31, merge, fgpartition)
 x33 = matcher(x32, FIVE)
 x34 = fork(both, x23, x27)
 x35 = fork(both, x30, x33)
 x36 = fork(both, x34, x35)
 x37 = height(I)
 x38 = subtract(x37, THREE)
 x39 = interval(ONE, x38, ONE)
 x40 = width(I)
 x41 = subtract(x40, THREE)
 x42 = interval(ONE, x41, ONE)
 x43 = multiply(SEVEN, UNITY)
 x44 = lbind(crop, I)
 x45 = rbind(x44, x43)
 x46 = chain(x36, x45, decrement)
 x47 = product(x39, x42)
 x48 = sfilter(x47, x46)
 x49 = matcher(first, x0)
 x50 = compose(flip, x49)
 x51 = rbind(sfilter, x50)
 x52 = compose(x51, dmirror)
 x53 = fork(combine, x51, x52)
 x54 = compose(x51, cmirror)
 x55 = compose(x51, hmirror)
 x56 = compose(x51, vmirror)
 x57 = fork(combine, x55, x56)
 x58 = fork(combine, x54, x57)
 x59 = fork(combine, x53, x58)
 x60 = multiply(FOUR, UNITY)
 x61 = rbind(add, x60)
 x62 = fork(insert, x61, initset)
 x63 = compose(backdrop, x62)
 x64 = rbind(toobject, I)
 x65 = chain(x59, x64, x63)
 x66 = mapply(x65, x48)
 x67 = paint(I, x66)
 return x67
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]