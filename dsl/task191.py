ONE = 1
UNITY = (1, 1)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def color(
 obj
):
 return next(iter(obj))[0]
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def initset(
 value
):
 return frozenset({value})
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def maximum(
 container
):
 return max(container, default=0)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
F = False
T = True
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
def occurrences(
 grid,
 obj
):
 occurrences = set()
 normed = normalize(obj)
 h, w = len(grid), len(grid[0])
 for i in range(h):
  for j in range(w):
   occurs = True
   for v, (a, b) in shift(normed, (i, j)):
    if 0 <= a < h and 0 <= b < w:
     if grid[a][b] != v:
      occurs = False
      break
    else:
     occurs = False
     break
   if occurs:
    occurrences.add((i, j))
 return frozenset(occurrences)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
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
def trim(
 grid
):
 return tuple(r[1:-1] for r in grid[1:-1])
def verify_task191(I):
 x0 = partition(I)
 x1 = compose(maximum, shape)
 x2 = argmin(x0, x1)
 x3 = color(x2)
 x4 = palette(I)
 x5 = remove(x3, x4)
 x6 = lbind(colorcount, I)
 x7 = argmin(x5, x6)
 x8 = mostcolor(I)
 x9 = shape(I)
 x10 = increment(x9)
 x11 = increment(x10)
 x12 = canvas(x8, x11)
 x13 = asobject(I)
 x14 = shift(x13, UNITY)
 x15 = paint(x12, x14)
 x16 = repeat(identity, ONE)
 x17 = astuple(cmirror, dmirror)
 x18 = astuple(hmirror, vmirror)
 x19 = combine(x17, x18)
 x20 = combine(x16, x19)
 x21 = fork(compose, first, last)
 x22 = product(x20, x20)
 x23 = apply(x21, x22)
 x24 = ofcolor(x15, x3)
 x25 = backdrop(x24)
 x26 = toobject(x25, x15)
 x27 = matcher(first, x7)
 x28 = rbind(sfilter, x27)
 x29 = matcher(first, x3)
 x30 = rbind(sfilter, x29)
 x31 = lbind(recolor, x8)
 x32 = compose(x31, x30)
 x33 = fork(combine, x28, x32)
 x34 = lbind(lbind, shift)
 x35 = lbind(occurrences, x15)
 x36 = compose(x35, x33)
 x37 = fork(mapply, x34, x36)
 x38 = lbind(chain, x37)
 x39 = lbind(x38, normalize)
 x40 = rbind(rapply, x26)
 x41 = initset(x39)
 x42 = lbind(rapply, x41)
 x43 = chain(first, x40, x42)
 x44 = mapply(x43, x23)
 x45 = paint(x15, x44)
 x46 = trim(x45)
 return x46
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]